from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, CategoryViewSet, TagViewSet

# Crear el router y registrar los ViewSets
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'categories', CategoryViewSet)  # Rutas para Categorías
router.register(r'tags', TagViewSet)  # Rutas para Tags

# Incluir las rutas en el archivo principal de URLs
urlpatterns = [
    path('', include(router.urls)),
]
