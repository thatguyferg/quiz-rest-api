def test_quizzes(test_client, init_db):

    response = test_client.get('/api/quiz')
    assert response.status_code == 200
    assert b"EZ Quiz" in response.data
