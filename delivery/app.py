from flask import flask

def create_app():
    app = Flask(__name__)
    return app