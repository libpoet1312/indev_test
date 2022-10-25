from rest_framework.test import APITestCase
from rest_framework import status

from answers.models import Answer
from categories.models import Category
from questions.models import Question


class ApiTests(APITestCase):
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

    def test_404(self):
        response = self.client.get('/question', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_200(self):
        response = self.client.get('/api/v1/categories/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question_list(self):
        response = self.client.get('/api/v1/questions/', format='json')
        self.assertIsInstance(response.data, dict)

    def test_question_list_with_params(self):
        response = self.client.get('/api/v1/questions/?limit=2&category=1&difficulty=1,2', format='json')
        self.assertIsInstance(response.data, dict)

    def test_question_detail(self):
        response = self.client.get('/api/v1/questions/1/', format='json')
        self.assertIsInstance(response.data, dict)

    def test_answer_for_no_validity(self):
        response = self.client.get('/api/v1/questions/1/Yes/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_answer_for_validity(self):
        response = self.client.get('/api/v1/questions/1/No/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)