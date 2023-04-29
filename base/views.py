from .forms import CreateUserForm
from django.shortcuts import render, redirect
from . import models
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    context = {}
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
    article = models.Article.objects.filter(category_id=id)
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


@login_required(login_url='login')
def createArticle(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {}
    context['form'] = form
    return render(request, 'article-form.html', context)


def updateArticle(request, id):
    context = {}
    article = models.Article.objects.get(id=id)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context['form'] = form

    return render(request, 'article-form.html', context)


def deleteArticle(request, id):
    context = {}
    article = models.Article.objects.get(id=id)
    if request.method == "POST":
        article.is_deleted = True
        article.save()
        return redirect('homepage')
    context['article'] = article

    return render(request, 'delete-article.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        try:
            user = models.User.objects.get(username=username)
            if user:
                auth = authenticate(
                    request,  username=username, password=password)
                if auth is not None:
                    login(request, auth)
                    return redirect("homepage")
                else:
                    messages.error(request, "password is not mathed")
            elif user.is_active == False:
                messages.error(request, "user is blocked")

        except models.User.DoesNotExist:
            messages.error(request, 'user does not exist')
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('homepage')


def registerUser(request):
    context = {}
    form = CreateUserForm()
    context['form'] = form

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect("homepage")
    else:
        messages.error(request, 'Error during register')
    return render(request, 'register.html', context)
