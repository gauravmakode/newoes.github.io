from rest_framework import serializers
from .models import exam, TestPaper, questions, TestIndex, UserAnswers, UserResult, flag, timer


class examSerializer(serializers.ModelSerializer):
    class Meta:
        model = exam
        fields = '__all__'


class TestPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPaper
        fields = '__all__'


class questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = '__all__'


class TestIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestIndex
        fields = '__all__'


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = '__all__'


class UserResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResult
        fields = '__all__'


class flagSerializer(serializers.ModelSerializer):
    class Meta:
        model = flag
        fields = '__all__'


class timerSerializer(serializers.ModelSerializer):
    class Meta:
        model = timer
        fields = '__all__'
