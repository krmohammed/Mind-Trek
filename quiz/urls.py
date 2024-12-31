from django.urls import path
from . import views


app_name = "quiz"

urlpatterns = [
    path("", views.quiz_home, name="quiz-home"),
    path("topics/", views.topics, name="topics"),
    path("quizzes/", views.quizzes, name="quizzes"),
    path("quizzes/quiz-details/<str:quiz_id>", views.quiz_details, name="quiz-details"),
    path("take-quiz/<str:quiz_id>", views.take_quiz, name="take-quiz"),
    path("quiz-summary/<str:quiz_id>", views.quiz_summary, name="quiz-summary"),
]
