from django.urls import path
from . import views


app_name = "quiz"

urlpatterns = [
    path("", views.quiz_home, name="quiz-home"),
    path("topics/", views.topics, name="topics"),
    path("quizzes/", views.quizzes, name="quizzes"),
]
