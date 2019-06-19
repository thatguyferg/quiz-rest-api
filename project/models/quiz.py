from marshmallow import fields


from . import db, ma


class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(175), unique=True, nullable=False)
    time_created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.TIMESTAMP, server_onupdate=db.func.current_timestamp())

    def __init__(self, name):
        self.name = name


class QuizSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)