from project import api
from project.resources.question import QuestionResource, QuestionsResource
from project.resources.quiz import QuizResource

# Route(s)
api.add_resource(QuizResource, '/quiz')
api.add_resource(QuestionsResource, '/question')
api.add_resource(QuestionResource, '/question/<int:quiz_id>')
