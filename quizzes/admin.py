from django.contrib import admin

from quizzes.models import Choice, Question, Quiz

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)