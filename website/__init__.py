from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from website.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from website.users.routes import users
    from website.restaurants.routes import restaurants
    from website.main.routes import main
    from website.errors.handlers import errors
    from website.foods.routes import foods

    app.register_blueprint(users)
    app.register_blueprint(restaurants)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(foods)

    from . import models

    with app.app_context():
        db.create_all()

    return app
