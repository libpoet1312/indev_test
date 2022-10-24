from rest_framework import filters
from rest_framework import mixins

from rest_framework.viewsets import GenericViewSet

from indev.paginators import CustomPagination
from questions.filters import MyCustomFilter
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

    filter_backends = [filters.SearchFilter, MyCustomFilter]
    search_fields = ['question']
