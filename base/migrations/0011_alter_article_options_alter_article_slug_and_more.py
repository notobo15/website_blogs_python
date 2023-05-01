# Generated by Django 4.1.7 on 2023-04-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_reply_comment_alter_reply_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(),
        ),
    ]