from flask import Flask

from .resources import api_bp
from project.models import db


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)

    return app

