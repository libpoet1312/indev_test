import requests

BASE_URL = 'https://the-trivia-api.com'


def get_questions():
    response = requests.get(BASE_URL + '/api/questions')
    if response.status_code == 200:
        return response.json()
    else:
        return []


def get_categories():
    response = requests.get(BASE_URL + '/api/categories')
    if response.status_code == 200:
        return response.json().keys()
    else:
        return []


categories = get_categories()
questions = get_questions()
print(questions)

