from flask import Flask
from .routes import users_bp
from .db import init_db


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongo:27017/flaskdb"

    init_db(app)
    app.register_blueprint(users_bp)

    return app
