from rest_framework import serializers
from .models import level, subject, topic, sheet_name, questions, index, UserAnswers, flag


class levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = level
        fields = '__all__'


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = '__all__'


class topicSerializer(serializers.ModelSerializer):
    class Meta:
        model = topic
        fields = '__all__'


class sheet_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = sheet_name
        fields = '__all__'


class questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = '__all__'


class indexSerializer(serializers.ModelSerializer):
    class Meta:
        model = index
        fields = '__all__'


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = '__all__'


class flagSerializer(serializers.ModelSerializer):
    class Meta:
        model = flag
        fields = '__all__'
