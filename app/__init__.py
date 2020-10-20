from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from app.config import Config
from app.auth import auth
from app.models import User


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return User.query(username)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    login_manager.init_app(app)
    app.register_blueprint(auth)
    return app
