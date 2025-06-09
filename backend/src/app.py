from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from classes import db
from routes import api

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

jwt = JWTManager(app)
CORS(app)

db.init_app(app)

app.register_blueprint(api)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )