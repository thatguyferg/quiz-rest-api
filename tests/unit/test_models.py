#Testing that the models for Quiz and Question are defined correctly using fixtures


def test_new_quiz(new_quiz):
    assert new_quiz.name == 'Nice Quiz'


def test_new_question(new_question):
    assert new_question.quiz_id == 1
    assert new_question.question_text == 'How nice is this quiz?'
    assert new_question.opt_a == 'Very nice'
    assert new_question.opt_b == 'Noice'
    assert new_question.opt_c == 'Goog'
    assert new_question.answer == 'Noice'

