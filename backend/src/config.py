from dotenv import load_dotenv
import os

load_dotenv()
class DevelopmentConfig():
    DEBUG=True
   
    #'SQLALCHEMY_DATABASE_URI': "mysql://root:password123@localhost/quicksters_db"
    #'SQLALCHEMY_TRACK_MODIFICATIONS': False
    JWT_SECRET_KEY = 'jwt-secret-string'
    MYSQL_HOST = 'db'  
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'  
    MYSQL_DB = 'quicksters_db'  
    
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False