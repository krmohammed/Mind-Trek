from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Quiz, UserQuizAttempt, UserAnswer, Answer
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
@login_required(login_url="quiz:quiz-home")
def quiz_home(request):
    return render(request, "quiz/home.html")

def topics(request):
    topics = Topic.objects.all()
    return render(request, "quiz/topics.html", {"topics": topics})

def quizzes(request):
    topics = Topic.objects.all()
    quizes = Quiz.objects.all().order_by("?")
    return render(request, "quiz/quizzes.html", {"quizzes": quizes, "topics": topics})

def quiz_details(request, quiz_id):
    quiz = Quiz.objects.get(id=int(quiz_id))
    return render(request, "quiz/quiz_details.html", {"quiz": quiz})

def take_quiz(request, quiz_id):
    
    return render(request, "quiz/take_quiz.html")


def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    # Get or create the user's quiz attempt
    attempt, created = UserQuizAttempt.objects.get_or_create(
        user=request.user, quiz=quiz
    )

    # Fetch all questions for the quiz
    questions = quiz.questions.all()
    total_questions = questions.count()

    # Get the current question index from the session
    current_question_index = request.session.get(f"quiz_{quiz.id}_current_question", 0)

    if current_question_index >= total_questions:
        # Quiz is complete
        return redirect("quiz:quiz-summary", quiz_id=quiz.id)

    # Get the current question
    current_question = questions[current_question_index]

    if request.method == "POST":
        # Handle the user's answer submission
        selected_answer_id = request.POST.get("answer")
        selected_answer = Answer.objects.filter(id=selected_answer_id).first()

        # Save the user's answer
        UserAnswer.objects.create(
            attempt=attempt,
            question=current_question,
            selected_answer=selected_answer,
        )

        # Move to the next question
        current_question_index += 1
        
        request.session[f"quiz_{quiz.id}_current_question"] = current_question_index

        # Redirect to the same view for the next question
        return redirect("quiz:take-quiz", quiz_id=quiz.id)

    # Fetch the possible answers for the current question
    answers = current_question.answers.all()

    context = {
        "quiz": quiz,
        "current_question": current_question,
        "answers": answers,
        "current_question_index": current_question_index + 1,  # 1-based index
        "total_questions": total_questions,
    }
    return render(request, "quiz/take_quiz.html", context)

def quiz_summary(request, quiz_id):
    return render(request, "quiz/quiz_summary.html")
