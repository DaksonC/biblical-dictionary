from django.test import TestCase
from words.models import Word
from words.api.serializers import WordSerializer


class WordSerializerTestCase(TestCase):
    def setUp(self):
        self.word_data = {
            'word': 'TestWord',
            'description': 'Test Description',
            'text_reference': 'Test Text Reference',
        }
        self.word = Word.objects.create(**self.word_data)
        self.serializer = WordSerializer(instance=self.word)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {
                         'id_word', 'word', 'description', 'text_reference', 'created_at', 'updated_at'})

    def test_serializer_field_values(self):
        data = self.serializer.data
        self.assertEqual(data['word'], self.word.word)
        self.assertEqual(data['description'], self.word.description)
        self.assertEqual(data['text_reference'], self.word.text_reference)
