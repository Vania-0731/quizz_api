from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, QuizAttempt
from quizzes.serializers import QuizSerializer

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer para crear o actualizar el perfil de un usuario.
    """
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar']
        read_only_fields = ['created_at']

class ProfileDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detallado para ver el perfil del usuario con detalles del usuario.
    """
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar', 'created_at']


class QuizAttemptSerializer(serializers.ModelSerializer):
    """
    Serializer para crear o actualizar un intento de quiz (con score, max_score, etc.)
    """
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'max_score']
        read_only_fields = ['completed_at']

class QuizAttemptDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detallado para ver un intento de quiz con detalles completos del usuario y quiz.
    """
    user = serializers.StringRelatedField()
    quiz = QuizSerializer()

    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'max_score', 'completed_at']
