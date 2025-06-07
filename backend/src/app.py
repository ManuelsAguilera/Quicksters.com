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