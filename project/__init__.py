from flask import Flask


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    from project.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from project.model import db
    db.init_app(app)

    return app

