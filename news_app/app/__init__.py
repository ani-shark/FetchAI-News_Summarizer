# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/posts_database.db'
    app.config['SQLALCHEMY_BINDS'] = {
        'users': 'sqlite:///../instance/user_database.db'
    }
    app.config['SECRET_KEY'] = 'adgjl2789'

    db.init_app(app)

    # Register Blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
