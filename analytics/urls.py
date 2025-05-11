from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionStatViewSet, QuizActivityViewSet

router = DefaultRouter()
router.register('question-stats', QuestionStatViewSet)
router.register('quiz-activities', QuizActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
