from flask import request, jsonify, Blueprint, redirect
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from classes import Usuario, Juego, Categoria, Speedrun, db
import bcrypt
import bleach
from sqlalchemy.orm import joinedload
import requests

from flask_mysqldb import MySQL
mysql = MySQL() 


api = Blueprint('api', __name__)

### ENDPOINTS

#GET test endpoints
@api.route('/')
def index():
    return redirect('/api/test')
    #return render_template('home.page.html')

@api.route('/api/test', methods=['GET'])
def test():
    return {'message': 'API funcionando!'}

@api.route('/api/testPost',methods=['POST'])
def testPost():
    data = request.get_json()
    return jsonify({
        'received': data,
        'status': 'success'
    })


##API Endpoints para Registro/Login/Autenticación
# post: /registro   ||| registra un usuario a la database
# post: /login ||| logea al usuario
# get: /profile ||| testeo para revisar si el token de JWT funciona correctamente

@api.route('/registro', methods=['POST'])
def register():
    try:
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser JSON'}), 400
        
        data = request.get_json()
        required_fields = ['username', 'correo', 'nacionalidad', 'contraseña']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400
        for key in data:
            if key not in required_fields:
                return jsonify({'error': f'Campo no permitido: {key}'}), 400
        
        if len(data['username'].strip()) < 3:
            return jsonify({'error': 'Nombre de usuario inválido'}), 400
        if '@' not in data['correo']:
            return jsonify({'error': 'Correo inválido'}), 400
        
        new_user = Usuario( 
            username = bleach.clean(data['username']),
            correo = bleach.clean(data['correo']),
            nacionalidad = bleach.clean(data['nacionalidad']),
            contraseña = bcrypt.hashpw(data['contraseña'].encode('utf-8'), bcrypt.gensalt())
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"msg": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/login', methods=['POST'])
def login():
    try:
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser JSON'}), 400
            
        data = request.get_json()
        required_fields = ['correo', 'contraseña']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400
        for key in data:
            if key not in required_fields:
                return jsonify({'error': f'Campo no permitido: {key}'}), 400

        if '@' not in data['correo']:
            return jsonify({'error': 'Correo inválido'}), 400
        
        correo = bleach.clean(data['correo'])
        contraseña = bleach.clean(data['contraseña'])
        
        user = Usuario.query.filter_by(correo=correo).first()
        if user and bcrypt.checkpw(contraseña.encode('utf-8'), user.contraseña.encode('utf-8')):
            access_token = create_access_token(identity=user.idusuario)
            return jsonify(access_token=access_token)
        else:
            return jsonify({"msg": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    try:
        user_id = get_jwt_identity()
        user = Usuario.query.get(user_id)
        if user:
            return jsonify(id=user.idusuario, username=user.username, correo=user.correo)
        else:
            return jsonify({"msg": "User not found"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

##REST API Endpoints para Usuario
# get: /db/users   ||| te da todos los usuarios
# get: /db/users/<nombreUsuario> ||| te da un usuario especifico
# post: /db/users, Content-Type: application/json ||| crea un usuario
# put: /db/users/<id>, Content-Type: application/json ||| actualiza un usuario
# delete: /db/users/<id> ||| elimina un usuario

@api.route('/db/users/<keyUsername>', methods=["GET"])
def getUser(keyUsername):
    try:
        user = Usuario.query.filter_by(username=keyUsername).first()
        if user:
            return jsonify(user.to_json())
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/users', methods=["GET"])
def getUsers():
    try:
        users = Usuario.query.all()
        return jsonify({
            'status': 'success',
            'data': [user.to_json() for user in users],
            'message': 'Users retrieved successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api.route('/db/users', methods=["POST"])
def createUser():
    try:
        print("Accesed createUser endpoint")
        
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser JSON'}), 400
        

        data = request.get_json()
        required_fields = ['username', 'correo']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400

        # Crear nuevo usuario
        new_user = Usuario( 
            username=data['username'],
            correo=data['correo'],
            nacionalidad=data.get('nacionalidad'),  # Opcionales
            contraseña=data.get('contraseña')      
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_json()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/users/<int:id>', methods=["PUT"])
def updateUser(id):
    try:
        user = Usuario.query.get(id)
        if not user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.correo = data.get('correo', user.correo)
        user.nacionalidad = data.get('nacionalidad', user.nacionalidad)
        user.contraseña = data.get('contraseña', user.contraseña)
        
        db.session.commit()
        return jsonify(user.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/users/<int:id>', methods=["DELETE"])
def deleteUser(id):
    try:
        user = Usuario.query.get(id)
        if not user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

##REST APi Endpoints para juegos
# get: /db/juegos   ||| te da todos los juegos
# get: /db/juegos/<idjuego> ||| te da un juego especifico
# post: /db/juegos, Content-Type: application/json ||| crea un juego
# put: /db/juegos/<idjuego>, Content-Type: application/json ||| actualiza un juego
# delete: /db/juegos/<idjuego> ||| elimina un juego

@api.route('/db/juegos', methods=["GET"])
def getJuegos():
    try:
        juegos = Juego.query.all()
        return jsonify({
            'status': 'success',
            'data': [juego.to_json() for juego in juegos],
            'message': 'Juegos retrieved successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api.route('/db/juegos/<int:idjuego>', methods=["GET"])
def getJuego(idjuego):
    try:
        juego = Juego.query.get(idjuego)
        if not juego:
            return jsonify({'error': 'Juego no encontrado'}), 404
        return jsonify(juego.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/juegos', methods=["POST"])
def createJuego():
    try:
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser JSON'}), 400
        
        data = request.get_json()
        required_fields = ['juego', 'url_icono', 'url_banner']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400

        # Crear nuevo juego
        new_juego = Juego(
            juego=data['juego'],
            url_icono=data['url_icono'],
            url_banner=data['url_banner']
        )

        db.session.add(new_juego)
        db.session.commit()

        return jsonify(new_juego.to_json()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/juegos/<int:idjuego>', methods=["PUT"])
def updateJuego(idjuego):
    try:
        juego = Juego.query.get(idjuego)
        if not juego:
            return jsonify({'error': 'Juego no encontrado'}), 404
        
        data = request.get_json()
        juego.juego = data.get('juego', juego.juego)
        juego.url_icono = data.get('url_icono', juego.url_icono)
        juego.url_banner = data.get('url_banner', juego.url_banner)
        
        db.session.commit()
        return jsonify(juego.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/juegos/<int:idjuego>', methods=["DELETE"])
def deleteJuego(idjuego):
    try:
        juego = Juego.query.get(idjuego)
        if not juego:
            return jsonify({'error': 'Juego no encontrado'}), 404
        
        db.session.delete(juego)
        db.session.commit()
        return jsonify({'message': 'Juego eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/steam/<int:appid>', methods=['GET'])
def getSteamGame(appid):
    try:
        response = requests.get(
            f'https://store.steampowered.com/api/appdetails?appids={appid}',
            timeout=5
        )
        
        if not response.ok:
            return jsonify({'error': 'No se pudo conectar a Steam'}), 503

        data = response.json().get(str(appid), {})
        
        if not data.get('success'):
            return jsonify({'error': 'Juego no encontrado en Steam'}), 404

        game = data['data']
        
        return jsonify({
            'appid': appid,
            'nombre': game.get('name'),
            'header_image': game.get('header_image'),  # Portada
            'background': game.get('background_raw')#,      # Fondo/banner
            #'descripcion': game.get('short_description'),
            #'desarrollador': game.get('developers', [])
        }), 200
    
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout consultando a Steam'}), 504
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/juegos/steam/<int:appid>', methods=['POST'])
def importSteamGame(appid):
    try:
        response = requests.get(
            f'https://store.steampowered.com/api/appdetails?appids={appid}',
            timeout=5
        )
        
        if not response.ok:
            return jsonify({'error': 'No se pudo conectar a Steam'}), 503

        data = response.json().get(str(appid), {})
        
        if not data.get('success'):
            return jsonify({'error': 'Juego no encontrado en Steam'}), 404
        
        game = data['data']
        nombre = game.get('name')
        url_icono = game.get('header_image')
        url_banner = game.get('background_raw')

        # Validar si ya existe por nombre
        if Juego.query.filter_by(juego=nombre).first():
            return jsonify({'msg': 'El juego ya existe en la base de datos'}), 409

        nuevo_juego = Juego(
            juego=nombre,
            url_icono=url_icono,
            url_banner=url_banner
        )

        db.session.add(nuevo_juego)
        db.session.commit()

        return jsonify(nuevo_juego.to_json()), 201

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout consultando a Steam'}), 504
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/juegos/<int:idjuego>/completo', methods=["GET"])
def getJuegoConCategorias(idjuego):
    try:
        juego = Juego.query.options(joinedload(Juego.categorias)).filter_by(idjuego=idjuego).first()
        if not juego:
            return jsonify({'error': 'Juego no encontrado'}), 404

        return jsonify({
            'juego': juego.to_json(),
            'categorias': [categoria.to_json() for categoria in juego.categorias]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

##REST API Endpoints para categorias
# get: /db/categorias   ||| te da todas las categorias
# get: /db/categorias/<idCategoria> ||| te da una categoria especifica
# post: /db/categorias, Content-Type: application/json ||| crea una categoria
# put: /db/categorias/<idCategoria>, Content-Type: application/json ||| actualiza una categoria
# delete: /db/categorias/<idCategoria> ||| elimina una categoria

@api.route('/db/categorias', methods=["GET"])
def getCategorias():
    try:
        categorias = Categoria.query.options(
            joinedload(Categoria.juego)
        ).all()

        return jsonify({
            'status': 'success',
            'data': [c.to_json() for c in categorias],
            'message': 'Categorias retrieved successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# def getCategorias():
#     try:
#         categorias = Categoria.query.all()
#         return jsonify({
#             'status': 'success',
#             'data': [categoria.to_json() for categoria in categorias],
#             'message': 'Categorias retrieved successfully'
#         }), 200
#     except Exception as e:
#         return jsonify({
#             'status': 'error',
#             'message': str(e)
#         }), 500

@api.route('/db/categorias/<int:idCategoria>', methods=["GET"])
def getCategoria(idCategoria):
    try:
        categoria = Categoria.query.get(idCategoria)
        if not categoria:
            return jsonify({'error': 'Categoria no encontrada'}), 404
        return jsonify(categoria.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@api.route('/db/categorias', methods=["POST"])
def createCategoria():
    try:
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser JSON'}), 400
        
        data = request.get_json()
        required_fields = ['idJuego', 'nombre_categoria']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400

        # Crear nueva categoria
        new_categoria = Categoria(
            idJuego=data['idJuego'],
            nombre_categoria=data['nombre_categoria']
        )

        db.session.add(new_categoria)
        db.session.commit()

        return jsonify(new_categoria.to_json()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@api.route('/db/categorias/<int:idCategoria>', methods=["PUT"])
def updateCategoria(idCategoria):
    try:
        categoria = Categoria.query.get(idCategoria)
        if not categoria:
            return jsonify({'error': 'Categoria no encontrada'}), 404
        
        data = request.get_json()
        categoria.idJuego = data.get('idJuego', categoria.idJuego)
        categoria.nombre_categoria = data.get('nombre_categoria', categoria.nombre_categoria)
        
        db.session.commit()
        return jsonify(categoria.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/categorias/<int:idCategoria>', methods=["DELETE"])
def deleteCategoria(idCategoria):
    try:
        categoria = Categoria.query.get(idCategoria)
        if not categoria:
            return jsonify({'error': 'Categoria no encontrada'}), 404
        
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({'message': 'Categoria eliminada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

##REST API Endpoints para speedruns
# get: /db/speedruns   ||| te da todos los speedruns
# get: /db/speedruns/<idspeedrun> ||| te da un speedrun especifico
# post: /db/speedruns, Content-Type: application/json ||| crea un speedrun
# put: /db/speedruns/<idspeedrun>, Content-Type: application/json ||| actualiza un speedrun
# delete: /db/speedruns/<idspeedrun> ||| elimina un speedrun

@api.route('/db/speedruns', methods=["GET"])
def getSpeedruns():
    try:
        speedruns = Speedrun.query.all()
        return jsonify({
            'status': 'success',
            'data': [speedrun.to_json() for speedrun in speedruns],
            'message': 'Speedruns retrieved successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api.route('/db/speedruns/<int:idspeedrun>', methods=["GET"])
def getSpeedrun(idspeedrun):
    try:
        speedrun = Speedrun.query.get(idspeedrun)
        if not speedrun:
            return jsonify({'error': 'Speedrun no encontrado'}), 404
        return jsonify(speedrun.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/speedruns', methods=["POST"])
def createSpeedrun():
    try:
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser JSON'}), 400
        
        data = request.get_json()
        required_fields = ['idusuario', 'idcategoria', 'url', 'duracion', 'fecha']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400

        # Crear nuevo speedrun
        new_speedrun = Speedrun(
            idusuario=data['idusuario'],
            idcategoria=data['idcategoria'],
            url=data['url'],
            duracion=data['duracion'],
            fecha=data['fecha']
        )

        db.session.add(new_speedrun)
        db.session.commit()

        return jsonify(new_speedrun.to_json()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/speedruns/<int:idspeedrun>', methods=["PUT"])
def updateSpeedrun(idspeedrun):
    try:
        speedrun = Speedrun.query.get(idspeedrun)
        if not speedrun:
            return jsonify({'error': 'Speedrun no encontrado'}), 404
        
        data = request.get_json()
        speedrun.idusuario = data.get('idusuario', speedrun.idusuario)
        speedrun.idcategoria = data.get('idcategoria', speedrun.idcategoria)
        speedrun.url_video = data.get('url', speedrun.url_video)
        speedrun.verificado = data.get('verificado', speedrun.verificado)
        speedrun.duracion = data.get('duracion', speedrun.duracion)
        speedrun.fecha = data.get('fecha', speedrun.fecha)
        
        db.session.commit()
        return jsonify(speedrun.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/db/speedruns/<int:idspeedrun>', methods=["DELETE"])
def deleteSpeedrun(idspeedrun):
    try:
        speedrun = Speedrun.query.get(idspeedrun)
        if not speedrun:
            return jsonify({'error': 'Speedrun no encontrado'}), 404
        
        db.session.delete(speedrun)
        db.session.commit()
        return jsonify({'message': 'Speedrun eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route("/db/speedruns/juego/<int:id_juego>/categoria/<int:id_categoria>", methods=["GET"])
def obtener_speedruns(id_juego, id_categoria):
    runs = Speedrun.query.filter_by(
        idjuego=id_juego,
        idcategoria=id_categoria,
        verificado=True
    ).order_by(Speedrun.duracion.asc()).all()
    
    resultados = []
    for run in runs:
        resultados.append({
            "jugador": run.usuario.username,
            "duracion": run.duracion,
            "fecha": run.fecha.strftime("%Y-%m-%d"),
            "video_url": run.url_video
        })

    return jsonify(resultados)