from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "12:3456"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db.init_app((app))

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import Users

    create_database(app)

    return app

def create_database(app):
    if not path.exists('C:/Users/gkay/PycharmProjects/kimosabe2/instance/users.db'):
        with app.app_context():
            db.create_all()
        print('databse created')
