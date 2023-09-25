from django.test import TestCase
from django.utils import timezone
from factory import Faker
from factory.django import DjangoModelFactory
from words.models import Word


class WordFactory(DjangoModelFactory):
    class Meta:
        model = Word

    word = Faker('word')
    description = Faker('text')
    text_reference = Faker('text')


class WordModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        WordFactory.create_batch(3)

    def test_word_str_representation(self):
        word = Word.objects.first()
        self.assertEqual(str(word), word.word)

    def test_word_created_at(self):
        word = Word.objects.first()
        self.assertTrue(word.created_at <= timezone.now())

    def test_word_updated_at(self):
        word = Word.objects.first()
        self.assertTrue(word.updated_at <= timezone.now())
