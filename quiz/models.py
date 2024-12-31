from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """Model for categorizing quizzes into topics or subjects."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    """Model for quizzes, which belong to a specific topic."""
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quizzes')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Model for questions within a quiz."""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question in {self.quiz.title}"


class Answer(models.Model):
    """Model for answers to a question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer to {self.question.text}"


class UserQuizAttempt(models.Model):
    """Tracks which quizzes users have attempted."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='user_attempts')
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s attempt at {self.quiz.title}"


class UserAnswer(models.Model):
    """Tracks the user's selected answers for each question in a quiz."""
    attempt = models.ForeignKey(UserQuizAttempt, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Answer by {self.attempt.user.username} for {self.question.text}"
