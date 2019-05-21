from flask import Blueprint
from flask_restful import Api
from resources.quiz import QuizResource
from resources.question import QuestionResource, QuestionsResource

api_bp=Blueprint('api', __name__)
api=Api(api_bp)

#Route(s)
api.add_resource(QuizResource, '/quiz')
api.add_resource(QuestionsResource, '/question')
api.add_resource(QuestionResource, '/question/<int:quiz_id>')