from flask import request
from flask_restful import Resource

from project.model import db, Quiz, QuizSchema

quizzes_schema = QuizSchema(many=True)
quiz_schema = QuizSchema()


class QuizResource(Resource):
    def get(self):
        quizzes = Quiz.query.all()
        quizzes = quizzes_schema.dump(quizzes).data
        return {'status': 'success', 'data': quizzes}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = quiz_schema.load(json_data)
        if errors:
            return errors, 422
        quiz = Quiz.query.filter_by(name=data['name']).first()
        if quiz:
            return {'message': 'Quiz with that name already exists'}, 400
        quiz = Quiz(name=json_data['name'])
        db.session.add(quiz)
        db.session.commit()
        result = quiz_schema.dump(quiz).data
        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = quiz_schema.load(json_data)
        if errors:
            return errors, 422
        quiz = Quiz.query.filter_by(id=data['id']).first()
        if not quiz:
            return {'message': 'Quiz does not exist'}, 400
        quiz.name = data['name']
        db.session.commit()
        result = quiz_schema.dump(quiz).data
        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = quiz_schema.load(json_data, partial=True)
        if errors:
            return errors, 422
        quiz = Quiz.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = quiz_schema.dump(quiz).data
        return {"status": 'success', 'data': result}, 204
