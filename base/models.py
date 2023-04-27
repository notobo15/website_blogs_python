from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField



class Category(models.Model):
  name = models.CharField(max_length=200)
  slug = models.SlugField()
  def __str__(self):
    return self.name
  def isCategory(self, slug):
    if self.slug == slug: 
      return self.id
    else:
      return False
       
      
class Article(models.Model):
  title = models.CharField(max_length=200)
  desc = models.TextField()
  content = RichTextField()
  slug = models.SlugField(default=slugify(u'{title}'), null=True, blank=True)
  img = models.CharField(max_length=200)
  totalViews = models.IntegerField(default=0)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  user = models.ForeignKey(User, models.SET_NULL, null=True)
  category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.title

class Rating(models.Model):
  article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  numStar = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  def __str__(self):
    return  self.user.username + " : " + str(self.numStar) + "* : " + self.article.title 


class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  content = RichTextField(null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


class Reply(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_reply')
  comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, related_name='reply_to_user')
  content = RichTextField()
  # userReplyTo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)