from flask import Blueprint
from flask_restful import Api
from resources.quiz import quiz

api_bp=Blueprint('api', __name__)
api=Api(api_bp)

#Route(s)
api.add_resource(quiz, '/quiz')