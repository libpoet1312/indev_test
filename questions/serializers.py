from rest_framework import serializers

from questions.models import Question
from answers.serializers import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='answer_set', many=True)

    class Meta:
        model = Question
        fields = '__all__'
        depth = 2
