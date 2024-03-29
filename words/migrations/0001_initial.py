# Generated by Django 4.2.5 on 2023-09-20 23:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id_word', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('text_reference', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
