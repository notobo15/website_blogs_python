# Generated by Django 4.1.7 on 2023-04-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_article_category_id_article_user_rating_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
    ]