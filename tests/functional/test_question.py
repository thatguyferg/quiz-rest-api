import json

#A few json objects used in below testing to clear up test functions
new_question_json_1 = json.dumps({
    "quiz_id": "1",
    "question_text": "Who belongs in a museum?",
    "opt_a": "You",
    "opt_b": "Me",
    "opt_c": "Milly",
    "answer": "You"
})
new_question_bad_json = json.dumps({
    "quiz_id": "1",
    "question_text": 1885,
    "opt_a": "You",
    "opt_b": "Me",
    "opt_c": "Milly",
    "answer": "You"
})
new_question_json_bad_quizid = json.dumps({
    "quiz_id": "9",
    "question_text": "Who belongs in a museum?",
    "opt_a": "You",
    "opt_b": "Me",
    "opt_c": "Milly",
    "answer": "You"
})
new_question_json_put = json.dumps({
    "id": "3",
    "quiz_id": "1",
    "question_text": "Who will win Worlds 2019?",
    "opt_a": "G2",
    "opt_b": "FPX",
    "opt_c": "NA :)",
    "answer": "NA :)"
})
new_question_json_put_bad_questionid = json.dumps({
    "id": "8",
    "quiz_id": "1",
    "question_text": "Who will win Worlds 2019?",
    "opt_a": "G2",
    "opt_b": "FPX",
    "opt_c": "NA :)",
    "answer": "NA :)"
})

"""
GET TESTS - QUESTION BY QUIZID
"""

def test_question_get_by_quizid_success(test_client, init_db):

    quizid = 2
    response = test_client.get('/api/question/' + str(quizid))
    assert response.status_code == 200
    assert b"Where is Milly right now?" in response.data

"""
GET TESTS - ALL QUESTIONS
"""

def test_questions_get_success(test_client, init_db):

    response = test_client.get('/api/question')
    assert response.status_code == 200
    assert b"How nice is this quiz?" in response.data
    assert b"Where is Milly right now?" in response.data

"""
POST TESTS
"""

def test_question_post_success(test_client, init_db):

    response = test_client.post('/api/question', data = new_question_json_1)
    assert response.status_code == 201
    assert b"Who belongs in a museum?" in response.data

def test_question_post_not_json_fails(test_client, init_db):

    response = test_client.post('/api/question', data = "Who did this?")
    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data

def test_question_post_bad_json_fails(test_client, init_db):

    response = test_client.post('/api/question', data = new_question_bad_json)
    assert response.status_code == 422

def test_question_post_bad_quizid_fails(test_client, init_db):

    response = test_client.post('/api/question', data = new_question_json_bad_quizid)
    assert response.status_code == 400
    assert b"Quiz not found with that id" in response.data

"""
PUT TESTS
"""

def test_question_put_success(test_client, init_db):

    response = test_client.put('/api/question', data = new_question_json_put)
    assert response.status_code == 204
    change_response = test_client.get('/api/question')
    assert b"Who will win Worlds 2019?" in change_response.data

def test_question_put_not_json_fails(test_client, init_db):

    response = test_client.put('/api/question', data = "Yeeeeeehaw")
    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data

def test_question_put_bad_json_fails(test_client, init_db):

    response = test_client.put('/api/question', data = new_question_bad_json)
    assert response.status_code == 422

def test_question_put_bad_questionid_fails(test_client, init_db):

    response = test_client.put('/api/question', data = new_question_json_put_bad_questionid)
    assert response.status_code == 400
    assert b"Question does not exist" in response.data

"""
DELETE TESTS
"""

def test_question_delete_success(test_client, init_db):

    response = test_client.delete('/api/question', data = json.dumps({"id": "1"}))
    assert response.status_code == 204
    response_check = test_client.get('/api/question')
    assert not b"How nice is this quiz?" in response_check.data

def test_question_delete_not_json_fails(test_client, init_db):

    response = test_client.delete('/api/question', data = "Yeeeeeehaw")
    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data

def test_question_delete_bad_json_fails(test_client, init_db):

    response = test_client.delete('/api/question', data = new_question_bad_json)
    assert response.status_code == 422