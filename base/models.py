from datetime import datetime, timedelta
from unidecode import unidecode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from django.utils.text import slugify
# from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    is_deleted = models.BooleanField(default=0)

    def __str__(self):
        return self.name

    def isCategory(self, slug):
        if self.slug == slug:
            return self.id
        else:
            return False


class Article(models.Model):
    title = models.TextField()
    desc = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    # content = RichTextField()
    titleToSlug = slugify(u'{title}')
    slug = models.TextField(null=True, blank=True)
    img = models.CharField(max_length=200)
    totalViews = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=0)
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        str = unidecode(self.title)
        self.slug = slugify(str)
        super(Article, self).save(*args, **kwargs)


class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    numStar = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=0)

    def __str__(self):
        return self.user.username + " : " + str(self.numStar) + "* : " + self.article.title


class Comment(MPTTModel):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, null=True, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name="children")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = RichTextUploadingField(
        null=True, blank=True, config_name='commment')

    publish = models.DateTimeField(default=datetime.now())

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=0)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return f'{self.content}'
