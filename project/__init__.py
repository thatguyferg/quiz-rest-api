from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    from project.model import db
    db.init_app(app)

    from project.app import api
    api.init_app(app)


    return app

