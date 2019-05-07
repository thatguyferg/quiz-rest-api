from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
ma=Marshmallow()

class Quiz(db.Model):
    __tablename__='quizzes'
    