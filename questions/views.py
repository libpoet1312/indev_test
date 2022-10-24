from rest_framework import generics, filters
from rest_framework import viewsets, mixins

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from indev.paginators import CustomPagination
from questions.models import Question
from questions.serializers import QuestionSerializer


# class QuestionListView(generics.ListAPIView):
#     queryset = Question.objects.all().order_by('id')
#     serializer_class = QuestionSerializer
#     pagination_class = CustomPagination
#     filterset_fields = ['category', 'difficulty']
#
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     search_fields = ['question']


class QuestionViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer
    pagination_class = CustomPagination
    filterset_fields = ['category', 'difficulty']

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['question']
