from flask import Blueprint, request
from sqlalchemy import DateTime

from app.app import db
from app.models.Mensajes import Mensajes

hello = Blueprint('users', __name__)

@hello.route('/')
def home():
    return "Hello users"

@hello.route('/msj/add', methods=['POST'])
def addMessage():
    remitente_id = request.args('remitente_id')

    new_msj = Mensajes(remitente_id, remitente_id, remitente_id, 'Hola', DateTime.now)

    print(new_msj)
    db.session.add(new_msj)
    db.session.commit()

    return "SAVED"