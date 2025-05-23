# users/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Profile, QuizAttempt
from .serializers import (
    ProfileSerializer, ProfileDetailSerializer,
    QuizAttemptSerializer, QuizAttemptDetailSerializer
)

class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return QuizAttemptDetailSerializer
        return QuizAttemptSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProfileDetailSerializer
        return ProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @action(detail=True, methods=['get'])
    def user_profile(self, request, pk=None):
        user = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user)
        serializer = ProfileDetailSerializer(profile)
        return Response(serializer.data)
