from django.shortcuts import render
import math
from django.contrib.auth.decorators import login_required
from .models import Topic, Quiz, UserQuizAttempt, UserAnswer, Answer
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Sum


# Create your views here.
@login_required(login_url="quiz:quiz-home")
def quiz_home(request):
    attempts = UserQuizAttempt.objects.filter(user=request.user)
    points = attempts.aggregate(Sum("score", default=0))["score__sum"]
    
    total_max_points = 0

    # Iterate through each attempt
    for attempt in attempts:
        total_max_points += attempt.quiz.max_points()
        
    print(total_max_points)
    print(points)
        
    average_score = (points / total_max_points) * 100 if total_max_points > 0 else 0
        
    context = {
        "attempts": attempts.order_by('-completed_at')[0:3],
        "attempts_count": attempts.count(),
        "total_points": points,
        "average": average_score
    }
    return render(request, "quiz/home.html", context)

def topics(request):
    topics = Topic.objects.all()
    return render(request, "quiz/topics.html", {"topics": topics})

def quizzes(request):
    topics = Topic.objects.all().order_by('?')[:3]
    quizes = Quiz.objects.all().order_by("?")
    return render(request, "quiz/quizzes.html", {"quizzes": quizes, "topics": topics})

def quiz_details(request, quiz_id):
    quiz = Quiz.objects.get(id=int(quiz_id))
    try:
        attempts = UserQuizAttempt.objects.get(quiz=quiz, user=request.user)
    except:
        attempts = None
    # if attempts:
    #     return redirect('quiz:quiz-summary', quiz_id=quiz_id)
    context = {
        "quiz": quiz,
        "attempts": attempts,
        "max_points": quiz.max_points(),
    }
    return render(request, "quiz/quiz_details.html", context)


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
        request.session[f"quiz_{quiz.id}_current_question"] = 0
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
    answers = current_question.answers.all().order_by("?")
    # answers = Answer.objects.filter(question=current_question).order_by("?")

    context = {
        "quiz": quiz,
        "current_question": current_question,
        "answers": answers,
        "current_question_index": current_question_index + 1,  # 1-based index
        "total_questions": total_questions,
    }
    return render(request, "quiz/take_quiz.html", context)

def review_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    # correct = quiz.answers.all()
    attempt = UserQuizAttempt.objects.get(user=request.user, quiz=quiz)
    user_answers = UserAnswer.objects.filter(attempt=attempt)
    
    correct_answers = 0
    for i in user_answers:
        try:
            if i.selected_answer.is_correct:
                correct_answers += 1
        except:
            pass
    
    score = attempt.score / quiz.max_points()
    score = math.ceil(score * 100)
    context = {
        'attempt': attempt,
        'score': score,
        'quiz': quiz,
        'correct_answers': correct_answers,
        'user_answers': [answer.selected_answer for answer in user_answers],
    }
    return render(request, 'quiz/quiz_review.html', context)

def retake_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    attempt = UserQuizAttempt.objects.get(quiz=quiz, user=request.user)
    attempt.delete()
    return redirect('quiz:take-quiz', quiz_id=quiz_id)

def quiz_summary(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    attempt = UserQuizAttempt.objects.get(user=request.user, quiz=quiz)
    answers = UserAnswer.objects.filter(attempt=attempt)
    correct_answers = 0
    for i in answers:
        try:
            if i.selected_answer.is_correct:
                correct_answers += 1
        except:
            pass
    attempt.score = correct_answers * quiz.points_per_question
    attempt.save()
    wrong_answers = quiz.questions.all().count() - correct_answers
    score = attempt.score / quiz.max_points()
    score = math.ceil(score * 100)
    context = {
                "attempt": attempt,
                "score": score, 
                "correct_answers": correct_answers,
                "wrong_answers": wrong_answers
            }
    return render(request, "quiz/quiz_summary.html", context)
