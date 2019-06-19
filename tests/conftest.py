import pytest
from project import create_app
from project.model import db, Quiz, Question


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
    db.create_all()

