from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from words.models import Word


class WordIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_word(self):
        url = reverse('Words-list')
        data = {
            'word': 'IntegrationTestWord',
            'description': 'Integration Test Description',
            'text_reference': 'Integration Test Text Reference',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Word.objects.count(), 1)
        self.assertEqual(Word.objects.get().word, 'IntegrationTestWord')

    def test_get_word_list(self):
        Word.objects.create(
            word='TestWord1', description='Description1', text_reference='Reference1')
        Word.objects.create(
            word='TestWord2', description='Description2', text_reference='Reference2')
        url = reverse('Words-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
