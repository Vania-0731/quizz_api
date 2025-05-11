from rest_framework import viewsets
from .models import Category, Tag, Quiz
from .serializers import CategorySerializer, TagSerializer, QuizSerializer, QuizDetailSerializer

# ViewSet para Categorías
class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet para listar, crear, actualizar y eliminar categorías"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ViewSet para Tags
class TagViewSet(viewsets.ModelViewSet):
    """ViewSet para listar, crear, actualizar y eliminar tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# ViewSet para Quizzes
class QuizViewSet(viewsets.ModelViewSet):
    """ViewSet para listar, crear, actualizar y eliminar quizzes"""
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':  # Si la acción es obtener detalles, usamos el serializer detallado
            return QuizDetailSerializer
        return self.serializer_class
