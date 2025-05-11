from django.db import models
from quizzes.models import Question, Quiz

class QuestionStat(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='stats')
    attempts = models.IntegerField(default=0)
    correct_attempts = models.IntegerField(default=0)

    @property
    def success_rate(self):
        return (self.correct_attempts / self.attempts) * 100 if self.attempts > 0 else 0

    def __str__(self):
        return f"Stats for: {self.question.text[:30]}..."

class QuizActivity(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='activities')
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    starts = models.IntegerField(default=0)
    completions = models.IntegerField(default=0)

    class Meta:
        unique_together = ['quiz', 'date']

    def __str__(self):
        return f"{self.quiz.title} activity on {self.date}"
