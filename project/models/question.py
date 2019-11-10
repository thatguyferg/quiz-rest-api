from marshmallow import fields


from . import db, ma


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id', ondelete='CASCADE'), nullable=False)
    question_text = db.Column(db.String(125), nullable=False)
    opt_a = db.Column(db.String(40), nullable=False)
    opt_b = db.Column(db.String(40), nullable=False)
    opt_c = db.Column(db.String(40), nullable=False)
    answer = db.Column(db.String(40), nullable=False)
    last_update = db.Column(db.TIMESTAMP, server_onupdate=db.func.current_timestamp())

    def __init__(self, quiz_id, question_text, opt_a, opt_b, opt_c, answer):
        self.quiz_id = quiz_id
        self.question_text = question_text
        self.opt_a = opt_a
        self.opt_b = opt_b
        self.opt_c = opt_c
        self.answer = answer


class QuestionSchema(ma.Schema):
    id = fields.Integer()
    quiz_id = fields.Integer()
    question_text = fields.String()
    opt_a = fields.String()
    opt_b = fields.String()
    opt_c = fields.String()
    answer = fields.String()