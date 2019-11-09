import json

"""
GET TESTS
"""

def test_quiz_get(test_client, init_db):

    response = test_client.get('/api/quiz')
    assert response.status_code == 200
    assert b"EZ Quiz" in response.data

"""
POST TESTS
"""

def test_quiz_post(test_client, init_db):
    
    response = test_client.post('/api/quiz', data = json.dumps({'name': 'Ok then'}))
    assert response.status_code == 201
    assert b"Ok then" in response.data

def test_quiz_post_with_not_json_fails(test_client, init_db):

    response = test_client.post('/api/quiz', data = "Henlo")
    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data

def test_quiz_post_with_bad_json_fails(test_client, init_db):

    response = test_client.post('/api/quiz', data = json.dumps({'name': 6685}))
    assert response.status_code == 422

def test_quiz_post_already_exists_fails(test_client, init_db):

    response = test_client.post('/api/quiz', data = json.dumps({'name': 'EZ Quiz'}))
    assert response.status_code == 400
    assert b"Quiz with that name already exists" in response.data

"""
PUT TESTS
"""

def test_quiz_put_successful_modification(test_client, init_db):
    
    response = test_client.put('/api/quiz', data = json.dumps({'id': '1' , 'name': 'Boomers lol'}))
    assert response.status_code == 204
    change_response = test_client.get('/api/quiz')
    assert b"Boomers lol" in change_response.data

def test_quiz_put_bad_json_fails(test_client, init_db):

    response = test_client.put('/api/quiz', data = "Henlo")
    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data

def test_quiz_put_bad_json_fails_return_error(test_client, init_db):

    response = test_client.put('/api/quiz', data = json.dumps({'id': 'hello'}))
    assert response.status_code == 422

def test_quiz_put_quiz_does_not_exist_fails(test_client, init_db):

    response = test_client.put('/api/quiz', data = json.dumps({'id': '4', 'name': 'Whatever Name'}))
    assert response.status_code == 400
    assert b"Quiz does not exist" in response.data

"""
DELETE TESTS
"""

def test_quiz_delete_successful(test_client, init_db):

    response = test_client.delete('/api/quiz', data = json.dumps({'id': '3'}))
    assert response.status_code == 204
    response_check = test_client.get('/api/quiz')
    assert response_check.status_code == 200
    assert not b"Ok then" in response_check.data

def test_quiz_delete_no_data_input_fails(test_client, init_db):

    response = test_client.delete('/api/quiz', data = "")
    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data

def test_quiz_delete_bad_json_fails(test_client, init_db):
    
    response = test_client.delete('/api/quiz', data = json.dumps({'id': 'sssss'}))
    assert response.status_code == 422
    
