from django.http import HttpResponse
from django.test import TestCase, Client


class TestResponse(TestCase):
    def test_response_success(self):
        client = Client()
        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.headers['content-type'], "text/html; charset=UTF-8")
