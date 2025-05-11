from rest_framework import serializers
from .models import QuestionStat, QuizActivity

class QuestionStatSerializer(serializers.ModelSerializer):
    success_rate = serializers.ReadOnlyField()

    class Meta:
        model = QuestionStat
        fields = '__all__'

class QuizActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizActivity
        fields = '__all__'
