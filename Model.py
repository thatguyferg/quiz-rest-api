from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
ma=Marshmallow()

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(175), unique=True, nullable=False)
    time_created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.TIMESTAMP, server_onupdate=db.func.current_timestamp())

    def __init__(self, name):
        self.name = name


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id', ondelete='CASCADE'), nullable=False)
    quiz = db.relationship('Quiz', backref=db.backref('questions', lazy='dynamic'))
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


class QuizSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)


