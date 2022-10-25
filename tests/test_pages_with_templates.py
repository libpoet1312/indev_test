from django.test import TestCase
from rest_framework import status

from answers.models import Answer
from categories.models import Category
from questions.models import Question

from questions.filters import MyCustomFilter


class ApiTests(TestCase):
    """
    Set up test db
    """
    def setUp(self):
        category = Category.objects.create(title='Arts')
        question = Question.objects.create(
            question='Are you ok?',
            difficulty='0',
            category=category
        )
        Answer.objects.create(text='No', correct=True, question=question)
        Answer.objects.create(text='Yes', correct=False, question=question)

    def test_questions_page(self):
        response = self.client.get('/questions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_question_page(self):
        response = self.client.get('/questions/1/')
        self.assertIsNotNone(response.context['question'])
