from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, QuizAttempt
from quizzes.serializers import QuizSerializer  # Asegúrate de importar el serializer para Quiz (si lo tienes)

# -------------------------------
# Serializer para el modelo Profile
# -------------------------------

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer para crear o actualizar el perfil de un usuario.
    """
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar']
        read_only_fields = ['created_at']  # Para garantizar que created_at no sea modificado

class ProfileDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detallado para ver el perfil del usuario con detalles del usuario.
    """
    user = serializers.StringRelatedField()  # Mostrar el nombre de usuario en lugar del ID

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar', 'created_at']


# -------------------------------
# Serializer para el modelo QuizAttempt
# -------------------------------

class QuizAttemptSerializer(serializers.ModelSerializer):
    """
    Serializer para crear o actualizar un intento de quiz (con score, max_score, etc.)
    """
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'max_score']
        read_only_fields = ['completed_at']  # Para garantizar que completed_at no sea modificado automáticamente

class QuizAttemptDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detallado para ver un intento de quiz con detalles completos del usuario y quiz.
    """
    user = serializers.StringRelatedField()  # Mostrar el nombre de usuario en lugar del ID
    quiz = QuizSerializer()  # Detalles completos del quiz relacionado (usa el QuizSerializer si tienes uno)

    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'max_score', 'completed_at']
