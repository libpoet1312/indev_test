from rest_framework.views import APIView
from rest_framework import generics

from questions.models import Question
from questions.serializers import QuestionSerializer


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


