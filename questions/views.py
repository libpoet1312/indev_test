from django.http import JsonResponse
from rest_framework import filters
from rest_framework import mixins
from rest_framework.generics import get_object_or_404

from rest_framework.viewsets import GenericViewSet
from django.views.generic import TemplateView

from random import shuffle

from indev.paginators import CustomPagination
from questions.filters import MyCustomFilter
from questions.models import Question
from questions.serializers import QuestionSerializer
from answers.models import Answer


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


def checkAnswerForQuestion(request, question_id, answer_text):
    """
    Check if given answer is correct
    """
    question = get_object_or_404(Question, id=question_id)
    correctAnswer = Answer.objects.filter(question=question).get(correct=True)
    if correctAnswer.text == answer_text:
        return JsonResponse({'correct': True}, status=200)
    else:
        return JsonResponse({'correct': False}, status=404)


# Template Views
class QuestionDetailView(TemplateView):
    template_name = "question.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        if kwargs['question_id']:
            question = Question.objects.get(id=kwargs['question_id'])
            context['id'] = question.id
            context['title'] = question.question
            context['difficulty'] = question.difficulty
            context['category'] = question.category
            answers = list(Answer.objects.filter(question_id__exact=question.id))

            # Random order of answers
            shuffle(answers)
            context['answers'] = answers
        return context
