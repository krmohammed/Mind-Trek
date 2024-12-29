from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Quiz


# Create your views here.
@login_required(login_url="quiz:quiz-home")
def quiz_home(request):
    return render(request, "quiz/home.html")

def topics(request):
    topics = Topic.objects.all()
    return render(request, "quiz/topics.html", {"topics": topics})

def quizzes(request):
    topics = Topic.objects.all()
    quizes = Quiz.objects.all().order_by("-topic__name", "-title")
    return render(request, "quiz/quizzes.html", {"quizzes": quizes, "topics": topics})

