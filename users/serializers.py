# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, QuizAttempt
from quizzes.serializers import QuizSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar']
        read_only_fields = ['created_at']

class ProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar', 'created_at']


class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'max_score']
        read_only_fields = ['completed_at']

class QuizAttemptDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    quiz = QuizSerializer()

    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'max_score', 'completed_at']
