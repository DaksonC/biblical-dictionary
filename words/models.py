from django.db import models
from uuid import uuid4


class Word(models.Model):
    id_word = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    word = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    text_reference = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["word"]

    def __str__(self):
        return self.word
