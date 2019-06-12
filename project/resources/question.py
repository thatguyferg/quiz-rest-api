from flask import request
from flask_restful import Resource

from project.model import db, Question, QuestionSchema, Quiz

questions_schema = QuestionSchema(many=True)
question_schema = QuestionSchema()


class QuestionsResource(Resource):
    def get(self):
        questions = Question.query.all()
        questions = questions_schema.dump(questions).data
        return {"status": "success", "data": questions}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # validate and deserialize
        data, errors = question_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        quiz_id = Quiz.query.filter_by(id=data['quiz_id']).first()
        if not quiz_id:
            return {"status": 'error', 'message': 'Quiz not found with that id'}, 400
        question = Question(
            quiz_id=data['quiz_id'],
            question_text=data['question_text'],
            opt_a=data['opt_a'],
            opt_b=data['opt_b'],
            opt_c=data['opt_c'],
            answer=data['answer']
        )
        db.session.add(question)
        db.session.commit()
        result = question_schema.dump(question).data
        return {'status': "success", 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data'}, 400
        # validate and deserialize
        data, errors = question_schema.load(json_data)
        if errors:
            return errors, 422
        question = Question.query.filter_by(id=data['id']).first()
        if not question:
            return {'message': 'Question does not exist'}, 400
        question.question_text = data['question_text']
        question.opt_a = data['opt_a']
        question.opt_b = data['opt_b']
        question.opt_c = data['opt_c']
        question.answer = data['answer']
        question.quiz_id = data['quiz_id']
        db.session.commit()
        result = question_schema.dump(question).data
        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = question_schema.load(json_data)
        if errors:
            return errors, 422
        question = Question.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = question_schema.dump(question).data
        return {"status": 'success', 'data': result}, 204


class QuestionResource(Resource):
    def get(self, quiz_id):
        quizQuestions = Question.query.filter_by(quiz_id=quiz_id).all()
        quizQuestions = questions_schema.dump(quizQuestions).data
        return {"status": "success", "data": quizQuestions}, 200
