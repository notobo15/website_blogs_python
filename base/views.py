from django.shortcuts import render
from . import models
from .forms import ArticleForm

users = [
    {"id": 1, "name": "user1"},
    {"id": 2, "name": "user2"},
    {"id": 3, "name": "user3"},
    {"id": 4, "name": "user4"},
    {"id": 5, "name": "user5"},
]
# Create your views here.
def homepage(request):
  context= {}
  category = models.Category.objects.all()
  context['category'] = category
  return render(request, 'homepage.html', context)
def category(request, pk):
  category = None
  article = None
  context = {}
  if models.Category.objects.filter(slug=pk).exists():
    category = models.Category.objects.get(slug=pk)
  id = 0
  for cate in models.Category.objects.filter(slug=pk):
    if cate.isCategory(pk):
      id = cate.isCategory(pk)
      break
  article = models.Article.objects.filter(category_id = id)
  # print(article)
  context['article'] = article
  context['category'] = category
  return render(request, 'category.html', context)
def detail(request, pk, detail):
  context = {}
  if models.Article.objects.filter(slug=detail).exists():
    article = models.Article.objects.get(slug=detail)
  context['article'] = article
  # category = models.Category.objects.get(slug=pk)
  return render(request, 'detail.html', context)



def createArticle(request):
    form = ArticleForm()
    context = {}
    context['form'] = form
    return render(request, 'article-form.html', context)
