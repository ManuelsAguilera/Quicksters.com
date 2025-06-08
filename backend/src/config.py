from dotenv import load_dotenv
import os

load_dotenv()
class DevelopmentConfig():
    DEBUG=True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    #'SQLALCHEMY_DATABASE_URI': "mysql://root:password123@localhost/quicksters_db"
    #'SQLALCHEMY_TRACK_MODIFICATIONS': False
    JWT_SECRET_KEY = 'jwt-secret-string'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'quicksters_db'
    JWT_SECRET_KEY = 'your_secret_key_here'
    