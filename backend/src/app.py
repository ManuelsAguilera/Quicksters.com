from flask import Flask, render_template, jsonify,request
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



### ENDPOINTS

#GET test endpoints
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
# get: /neon/users/<nombreUsuario>
# post: /neon/users, Content-Type: application/json
# put: /neon/users/<id>, Content-Type: application/json
# delete: /neon/users/<id>

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




##Esto va al final de todos los endpoints


if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()