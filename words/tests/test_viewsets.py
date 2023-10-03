from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from words.models import Word
from words.api.serializers import WordSerializer


class WordViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.word_data = {'word': 'TestWord',
                          'description': 'Test Description',
                          'text_reference': 'Test Text Reference', }
        self.word = Word.objects.create(
            word='TestWord ', description='TestDescription', text_reference='TestTextReference')
        self.serializer = WordSerializer(instance=self.word)

    def test_get_word_list(self):
        response = self.client.get('/api/v1/words/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_word_detail(self):
        response = self.client.get(f'//api/v1/words/{self.word.id_word}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)
