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

    def test_create_word(self):
        response = self.client.post('/words/', self.word_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assuming there's an existing Word object
        self.assertEqual(Word.objects.count(), 2)

    def test_get_word_list(self):
        response = self.client.get('/words/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_word_detail(self):
        response = self.client.get(f'/words/{self.word.id_word}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)

    def test_update_word(self):
        updated_data = {'word': 'UpdatedWord', 'description': 'Test Description',
                        'text_reference': 'Test Text Reference', }
        response = self.client.put(
            f'/words/{self.word.id_word}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.word.refresh_from_db()
        self.assertEqual(self.word.word, 'UpdatedWord')

    def test_delete_word(self):
        response = self.client.delete(f'/words/{self.word.id_word}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Word.objects.count(), 0)
