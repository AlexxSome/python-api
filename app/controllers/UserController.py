from flask import jsonify, Blueprint, request
from app.app import db
from app.models.Usuario import Usuario, UsuarioSchema

userController = Blueprint('userController', __name__)


@userController.route('/users', methods=['GET'])
def obtener_usuarios():
    users = db.session.execute(db.select(Usuario)).scalars()
    usuarios_json = []
    for usuario in users:
        usuario_json = {
            'id': usuario.id,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'email': usuario.email,
            'rol': usuario.rol,
            'fecha_registro': usuario.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')
        }
        usuarios_json.append(usuario_json)
    return jsonify(usuarios_json)


@userController.get('/users2')
def get_users_with_marshmallow():
    users = db.session.execute(db.select(Usuario)).scalars()
    users_schema = UsuarioSchema(many=True)
    result = users_schema.dump(users)

    return jsonify(result)


@userController.post('/user/create')
def create_user():
    data = request.json
    obj = Usuario(**data)

    db.session.add(obj)
    db.session.commit()

    return obj.__repr__()
