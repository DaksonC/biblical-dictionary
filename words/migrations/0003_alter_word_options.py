# Generated by Django 4.2.5 on 2023-10-03 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_alter_word_word'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['word']},
        ),
    ]
