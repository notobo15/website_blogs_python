# Generated by Django 4.1.7 on 2023-05-10 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_article_liked_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-publish', '-created']},
        ),
    ]
