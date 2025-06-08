from flask import Flask, render_template, jsonify,request,redirect
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from classes import db, mysql
from routes import api
from auth import auth

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

jwt = JWTManager(app)
CORS(app)

mysql.init_app(app)
db.init_app(app)

app.register_blueprint(api)
app.register_blueprint(auth)

#with app.app_context():
#        db.create_all()

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    # Configure server
    app.run(
        debug=True,        # Enable debug mode
        host='0.0.0.0',   # Listen on all available interfaces
        port=5000         # Specify port explicitly
    )