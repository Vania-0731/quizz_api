from rest_framework import serializers
from .models import Quiz, Question, Choice
from categories.serializers import CategorySerializer, TagSerializer
from categories.models import Category, Tag


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer for the Choice model with question reference"""
    question_id = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        source='question',
        write_only=True
    )
    question = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct', 'question', 'question_id']



class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for the Question model"""
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Serializer for Question model with nested choices"""
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'category', 'tags']


class QuizDetailSerializer(serializers.ModelSerializer):
    """Serializer for Quiz model with nested questions, category, and tags"""
    questions = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = [ 'id', 'title', 'description', 'created_at', 'category', 'tags', 'questions', ]

    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionDetailSerializer(questions, many=True).data


class AnswerSerializer(serializers.Serializer):
    """Serializer for answer validation"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()
