import os
import sys
from pathlib import Path

import requests
import django
from environ import environ

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env.dev'))

if env('DEBUG'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.dev')

django.setup()

from categories.models import Category
from answers.models import Answer
from questions.models import Question

BASE_URL = 'https://the-trivia-api.com'


def fetch_questions():
    response = requests.get(BASE_URL + '/api/questions')
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_categories():
    response = requests.get(BASE_URL + '/api/categories')
    if response.status_code == 200:
        return response.json().keys()
    else:
        return []


def load_categories(categories_list):
    for category in categories_list:
        data = {
            'title': category
        }
        Category.objects.get_or_create(**data)

    sys.stdout.write('[+] Loaded categories: OK\n')


def load_answers_and_questions(questions_list):
    for question in questions_list:
        category = Category.objects.all().get(title=question['category'])

        data = {
            'question': question['question'],
            'difficulty': 0 if question['difficulty'] == 'easy' else 1 if question['difficulty'] == 'medium' else 2,
            'category': category
        }

        created_question_obj, created = Question.objects.get_or_create(**data)

        if question['type'] == 'Multiple Choice':
            answers_list = [(question['correctAnswer'], 1)] + [(x, 0) for x in question['incorrectAnswers']]
            load_answers_to_question_obj(created_question_obj, answers_list)

    sys.stdout.write('[+] Loaded Questions: OK\n')


def load_answers_to_question_obj(question_obj, answers):
    for answer in answers:
        data = {
            'text': answer[0],
            'correct': answer[1],
            'question': question_obj
        }
        Answer.objects.get_or_create(**data)

    sys.stdout.write(f'[+] Loaded Answers for question {question_obj}: OK\n')


if __name__ == '__main__':
    sys.stdout.write('Loading demo data to database...\n')
    categories = fetch_categories()
    questions = fetch_questions()

    load_categories(categories)
    load_answers_and_questions(questions)
