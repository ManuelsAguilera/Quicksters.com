class DevelopmentConfig():
    DEBUG=True
   
    JWT_SECRET_KEY = 'jwt-secret-string'
    MYSQL_HOST = 'db'  
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'  
    MYSQL_DB = 'quicksters_db'  
    
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False