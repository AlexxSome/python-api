from app.utils.db import db


class Mensajes(db.Model):
    __tablename__ = 'mensajes'
    id = db.Column(db.Integer, primary_key=True)
    remitente_id = db.Column(db.Integer)
    destinatario_id = db.Column(db.Integer)
    mensaje = db.Column(db.String(250))
    fecha_hora = db.Column(db.DateTime)

    def __init__(self, id, remitente_id, destinatario_id, mensaje, fecha_hora):
        self.id = id
        self.remitente_id = remitente_id
        self.destinatario_id = destinatario_id
        self.mensaje = mensaje
        self.fecha_hora = fecha_hora
