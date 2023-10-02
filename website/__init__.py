from flask import Flask, render_template, request, flash

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '123456'

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app