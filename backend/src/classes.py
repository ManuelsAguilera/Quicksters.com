from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

mysql = MySQL()
db = SQLAlchemy()

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
    idJuego = db.Column(db.Integer, db.ForeignKey('juegos.idjuego'), nullable=False)
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
    
