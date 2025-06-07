from flask import Flask, render_template, jsonify,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

from dotenv import load_dotenv
import os



    



load_dotenv()
app = Flask(__name__)
app.config.from_object(config['development'])


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)


CORS(app)


#Classes
#Tabla usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    idusuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    nacionalidad = db.Column(db.String(100))
    contraseña = db.Column(db.String(20), nullable=True) 
    def to_json(self):
        return {
            'idusuario': self.idusuario,
            'username': self.username,
            'correo': self.correo,
            'nacionalidad': self.nacionalidad,
            'contraseña': self.contraseña
        }

#Tabla juegos
class Juego(db.Model):
    __tablename__ = 'juegos'
    idjuego = db.Column(db.Integer, primary_key=True)
    nombre_juego = db.Column(db.String(100), nullable=False)
    url_icono = db.Column(db.String(255))
    url_banner = db.Column(db.String(255))

    def to_json(self):
        return {
            'idjuego': self.idjuego,
            'nombre_juego': self.nombre_juego,
            'url_icono': self.url_icono,
            'url_banner': self.url_banner
        }

#Tabla juegos
class Categoria(db.Model):
    __tablename__ = 'categoria'
    idCategoria = db.Column(db.Integer, primary_key=True)
    idJuego = db.Column(db.Integer, nullable=False)
    nombre_categoria = db.Column(db.String(100), nullable=False)
    juego = db.relationship('Juego', backref='categorias', lazy=True)
    def to_json(self):
        return {
            'idCategoria': self.idCategoria,
            'idjuego': self.idjuego,
            'nombre_categoria': self.nombre_categoria,
            'juego': self.juego.to_json() if self.juego else None     
        }

#Tabla speedrun
class Speedrun(db.Model):
    __tablename__ = 'speedrun'
    idspeedrun = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'), nullable=False)
    idcategoria = db.Column(db.Integer, db.ForeignKey('categoria.idCategoria'), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    verificado = db.Column(db.Boolean, default=False)
    duracion = db.Column(db.Interval, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    usuario = db.relationship('Usuario', backref='speedruns', lazy=True)
    categoria = db.relationship('Categoria', backref='speedruns', lazy=True)
    def to_json(self):
        return {
            'idspeedrun': self.idspeedrun,
            'idusuario': self.idusuario,
            'idcategoria': self.idcategoria,
            'url': self.url,
            'verificado': self.verificado,
            'duracion': str(self.duracion),
            'fecha': self.fecha.isoformat(),
            'usuario': self.usuario.to_json() if self.usuario else None,
            'categoria': self.categoria.to_json() if self.categoria else None
        }
    


### ENDPOINTS

#GET test endpoints
@app.route('/')
def index():
    return redirect('/api/test')

@app.route('/api/test', methods=['GET'])
def test():
    return {'message': 'API funcionando!'}

@app.route('/api/testPost',methods=['POST'])
def testPost():
    data = request.get_json()
    return jsonify({
        'received': data,
        'status': 'success'
    })


##REST API Endpoints para Usuario
# get: /neon/users   ||| te da todos los usuarios
# get: /neon/users/<nombreUsuario> ||| te da un usuario especifico
# post: /neon/users, Content-Type: application/json ||| crea un usuario
# put: /neon/users/<id>, Content-Type: application/json ||| actualiza un usuario
# delete: /neon/users/<id> ||| elimina un usuario

@app.route('/neon/users/<keyUsername>', methods=["GET"])
def getUser(keyUsername):
    try:
        user = Usuario.query.filter_by(username=keyUsername).first()
        if user:
            return jsonify(user.to_json())
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/neon/users', methods=["GET"])
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


@app.route('/neon/users', methods=["POST"])
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

@app.route('/neon/users/<int:id>', methods=["PUT"])
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

@app.route('/neon/users/<int:id>', methods=["DELETE"])
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
# get: /neon/juegos   ||| te da todos los juegos
# get: /neon/juegos/<idjuego> ||| te da un juego especifico
# post: /neon/juegos, Content-Type: application/json ||| crea un juego
# put: /neon/juegos/<idjuego>, Content-Type: application/json ||| actualiza un juego
# delete: /neon/juegos/<idjuego> ||| elimina un juego

@app.route('/neon/juegos', methods=["GET"])
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

@app.route('/neon/juegos/<int:idjuego>', methods=["GET"])
def getJuego(idjuego):
    try:
        juego = Juego.query.get(idjuego)
        if not juego:
            return jsonify({'error': 'Juego no encontrado'}), 404
        return jsonify(juego.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/neon/juegos', methods=["POST"])
def createJuego():
    try:
        if not request.is_json:
            return jsonify({'error': 'El cuerpo de la solicitud debe ser JSON'}), 400
        
        data = request.get_json()
        required_fields = ['nombre_juego', 'url_icono', 'url_banner']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400

        # Crear nuevo juego
        new_juego = Juego(
            nombre_juego=data['nombre_juego'],
            url_icono=data['url_icono'],
            url_banner=data['url_banner']
        )

        db.session.add(new_juego)
        db.session.commit()

        return jsonify(new_juego.to_json()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/neon/juegos/<int:idjuego>', methods=["PUT"])
def updateJuego(idjuego):
    try:
        juego = Juego.query.get(idjuego)
        if not juego:
            return jsonify({'error': 'Juego no encontrado'}), 404
        
        data = request.get_json()
        juego.nombre_juego = data.get('nombre_juego', juego.nombre_juego)
        juego.url_icono = data.get('url_icono', juego.url_icono)
        juego.url_banner = data.get('url_banner', juego.url_banner)
        
        db.session.commit()
        return jsonify(juego.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/neon/juegos/<int:idjuego>', methods=["DELETE"])
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

##REST API Endpoints para categorias
# get: /neon/categorias   ||| te da todas las categorias
# get: /neon/categorias/<idCategoria> ||| te da una categoria especifica
# post: /neon/categorias, Content-Type: application/json ||| crea una categoria
# put: /neon/categorias/<idCategoria>, Content-Type: application/json ||| actualiza una categoria
# delete: /neon/categorias/<idCategoria> ||| elimina una categoria

@app.route('/neon/categorias', methods=["GET"])
def getCategorias():
    try:
        categorias = Categoria.query.all()
        return jsonify({
            'status': 'success',
            'data': [categoria.to_json() for categoria in categorias],
            'message': 'Categorias retrieved successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/neon/categorias/<int:idCategoria>', methods=["GET"])
def getCategoria(idCategoria):
    try:
        categoria = Categoria.query.get(idCategoria)
        if not categoria:
            return jsonify({'error': 'Categoria no encontrada'}), 404
        return jsonify(categoria.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/neon/categorias', methods=["POST"])
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


@app.route('/neon/categorias/<int:idCategoria>', methods=["PUT"])
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

@app.route('/neon/categorias/<int:idCategoria>', methods=["DELETE"])
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
# get: /neon/speedruns   ||| te da todos los speedruns
# get: /neon/speedruns/<idspeedrun> ||| te da un speedrun especifico
# post: /neon/speedruns, Content-Type: application/json ||| crea un speedrun
# put: /neon/speedruns/<idspeedrun>, Content-Type: application/json ||| actualiza un speedrun
# delete: /neon/speedruns/<idspeedrun> ||| elimina un speedrun

@app.route('/neon/speedruns', methods=["GET"])
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

@app.route('/neon/speedruns/<int:idspeedrun>', methods=["GET"])
def getSpeedrun(idspeedrun):
    try:
        speedrun = Speedrun.query.get(idspeedrun)
        if not speedrun:
            return jsonify({'error': 'Speedrun no encontrado'}), 404
        return jsonify(speedrun.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/neon/speedruns', methods=["POST"])
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

@app.route('/neon/speedruns/<int:idspeedrun>', methods=["PUT"])
def updateSpeedrun(idspeedrun):
    try:
        speedrun = Speedrun.query.get(idspeedrun)
        if not speedrun:
            return jsonify({'error': 'Speedrun no encontrado'}), 404
        
        data = request.get_json()
        speedrun.idusuario = data.get('idusuario', speedrun.idusuario)
        speedrun.idcategoria = data.get('idcategoria', speedrun.idcategoria)
        speedrun.url = data.get('url', speedrun.url)
        speedrun.verificado = data.get('verificado', speedrun.verificado)
        speedrun.duracion = data.get('duracion', speedrun.duracion)
        speedrun.fecha = data.get('fecha', speedrun.fecha)
        
        db.session.commit()
        return jsonify(speedrun.to_json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/neon/speedruns/<int:idspeedrun>', methods=["DELETE"])
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



##Esto va al final de todos los endpoints


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    # Configure server
    app.run(
        debug=True,        # Enable debug mode
        host='0.0.0.0',   # Listen on all available interfaces
        port=5000         # Specify port explicitly
    )