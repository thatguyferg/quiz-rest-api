import pytest


from project import create_app
from project.models import db
from project.models.quiz import Quiz
from project.models.question import Question


@pytest.fixture(scope='module')
def new_quiz():
    quiz = Quiz('Nice Quiz')
    return quiz


@pytest.fixture(scope='module')
def new_question():
    question = Question(1, 'How nice is this quiz?', 'Very nice',
                        'Noice', 'Goog', 'Noice')
    return question


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('test_config.py')

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_db():
    db.drop_all()
    db.create_all()

    #Quiz and Question objects for testing
    quiz1 = Quiz('EZ Quiz')
    quiz2 = Quiz('Medium Quiz')

    db.session.add(quiz1)
    db.session.add(quiz2)
    db.session.commit()
    question = Question(quiz1.id, 'How nice is this quiz?', 'Very nice',
                        'Noice', 'Goog', 'Noice')
    db.session.add(question)

    db.session.commit()

    yield db

    