from django.test import TestCase

from categories.models import Category
from answers.models import Answer
from questions.models import Question


class QuestionsTests(TestCase):
    def setUp(self):
        category = Category.objects.create(title='Arts')
        question = Question.objects.create(
            question='Are you ok?',
            difficulty='0',
            category=category
        )
        Answer.objects.create(text='No', correct=True, question=question)
        Answer.objects.create(text='Yes', correct=False, question=question)

    def test_Question_str(self):
        question = Question.objects.get(question='Are you ok?')
        self.assertEqual(str(question), 'Are you ok?')

    def test_Answer_str(self):
        answer = Answer.objects.get(text='No', correct=True,)
        self.assertEqual(str(answer), 'No')

    def test_Category_str(self):
        category = Category.objects.get(title='Arts')
        self.assertEqual(str(category), 'Arts')


