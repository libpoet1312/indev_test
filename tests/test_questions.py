from rest_framework.test import APITestCase
from rest_framework import status


class QuestionsTests(APITestCase):
    """
    Set up test db
    """
    def setUp(self):
        pass

    def test_404(self):
        response = self.client.get('/question', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_200(self):
        response = self.client.get('/questions/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

