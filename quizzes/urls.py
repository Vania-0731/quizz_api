from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet
from categories.views import QuizViewSet, CategoryViewSet, TagViewSet


# Inicializamos el router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  # Rutas para Categorías
router.register(r'tags', TagViewSet)  # Rutas para Tags
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

# Definimos las rutas
urlpatterns = [
    path('', include(router.urls)),  # Incluimos las URLs definidas por el router
]
