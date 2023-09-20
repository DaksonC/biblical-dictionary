from django.db import models
from uuid import uuid4

# Create your models here.


class Word(models.Model):
    id_word = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    word = models.CharField(max_length=255)
    description = models.TextField()
    text_reference = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word
