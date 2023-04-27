from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# from django.utils.text import slugify
# from tinymce.models import HTMLField


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
    content = RichTextField()
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
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def setDelete(self):
        self.is_deleted = True
        return self.is_deleted


class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    numStar = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=0)

    def __str__(self):
        return self.user.username + " : " + str(self.numStar) + "* : " + self.article.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = RichTextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=0)


class Reply(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='user_reply')
    comment = models.ForeignKey(
        Comment, on_delete=models.SET_NULL, null=True, related_name='reply_to_user')
    content = RichTextField()
    # userReplyTo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=0)
