from classes import mysql
from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/registro', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    correo = data['correo']
    nacionalidad = data['nacionalidad']
    contraseña = data['contraseña']
    
    hashed_pw = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

    cur = mysql.connection.cursor()
    
    cur.execute("INSERT INTO `usuario` (`username`, `correo`, `nacionalidad`, `contraseña`) VALUES (%s, %s, %s, %s)",
                (username, correo, nacionalidad, hashed_pw))

    mysql.connection.commit()
    
    user_id = cur.lastrowid
    cur.close()

    return jsonify({"msg": "User registered successfully", "user_id": user_id}), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data['correo']
    contraseña = data['contraseña']

    cur = mysql.connection.cursor()
    cur.execute("SELECT idusuario, contraseña FROM usuario WHERE correo = %s", (correo,))
    user = cur.fetchone()
    cur.close()

    if user and bcrypt.checkpw(contraseña.encode('utf-8'), user[1].encode('utf-8')):
        access_token = create_access_token(identity=user[0])
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Invalid credentials"}), 401


@auth.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()

    cur = mysql.connection.cursor()
    cur.execute("SELECT idusuario, username, correo FROM usuario WHERE idusuario = %s", (user_id,))
    user = cur.fetchone()
    cur.close()

    if user:
        return jsonify(id=user[0], username=user[1], correo=user[2])
    else:
        return jsonify({"msg": "User not found"}), 404
