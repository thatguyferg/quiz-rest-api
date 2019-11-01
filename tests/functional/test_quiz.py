import json

def test_quiz_get(test_client, init_db):

    response = test_client.get('/api/quiz')
    assert response.status_code == 200
    assert b"EZ Quiz" in response.data

def test_quiz_post(test_client, init_db):
    
    response = test_client.post('/api/quiz', data = json.dumps({'name': 'Ok then'}))
    assert response.status_code == 201
    assert b"Ok then" in response.data

def test_quiz_with_bad_json_fails(test_client, init_db):

    response = test_client.post('/api/quiz', data = "Henlo")
    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data
