from datetime import datetime
from json import JSONEncoder

from flask_marshmallow import Marshmallow

from app.app import app
from app.utils.db import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    rol = db.Column(db.String)
    fecha_registro = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, nombre, apellido, email, password, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.rol = rol
        self.fecha_registro = datetime.now()

    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}', " \
               f"rol='{self.rol}', fecha_registro='{self.fecha_registro}')"

# class UsuarioEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__

ma = Marshmallow(app)

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'email', 'rol', 'fecha_registro')