from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api


from project.resources.question import QuestionResource, QuestionsResource
from project.resources.quiz import QuizResource

db = SQLAlchemy()
ma = Marshmallow()

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route(s)
api.add_resource(QuizResource, '/quiz')
api.add_resource(QuestionsResource, '/question')
api.add_resource(QuestionResource, '/question/<int:quiz_id>')


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    app.register_blueprint(api_bp, url_prefix='/api')

    from project.model import db
    db.init_app(app)

    return app


