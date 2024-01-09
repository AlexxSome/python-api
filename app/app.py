from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Clientflix'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    from app.routes.hello import hello
    from app.controllers.UserController import userController

    app.register_blueprint(userController)
    app.register_blueprint(hello)
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
