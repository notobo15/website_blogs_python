from .forms import CreateUserForm
from django.shortcuts import render, redirect
from . import models
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import re


def homepage(request):
    context = {}
    category = models.Category.objects.all()
    context['category'] = category
    return render(request, 'homepage.html', context)

def contact(request):
    return render(request, 'contact.html')


def category(request, pk):
    category = None
    other_categories = models.Category.objects.all()
    posts = models.Article.objects.order_by('-created')[:7]
    article = None
    context = {"other_categories" : other_categories, "posts" : posts}
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
            print("khong ton tai")
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
        if form.is_valid():
            print("valid")
            form.save()
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        isUserNameExsit = False
        isEmailExsit = False
        isPasswordMatched = False
        isPassword = False
        if len(password1.strip()) <= 8 or len(password2.strip()) <= 8:
            messages.error(request, 'Mật Khẩu Chứa Ít Nhất 8 Kí Tự')
        else:
            if password2 != password1:
                messages.error(request, 'Xác Nhận Mật Khẩu Không Trùng Khớp.')
            else:
                isPassword = True
        try:
            email = models.User.objects.get(email=email)
            messages.error(request, 'Email Này Đã Tồn Tại')
        except models.User.DoesNotExist:
            isEmailExsit = True
        try:
            user = models.User.objects.get(username=username)
            messages.error(request, 'Tên Tài Khoản Này Đã Tồn Tại')
        except models.User.DoesNotExist:
            regex = r'^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*$'
            print(re.search(regex, username))
            if re.search(regex, username):
                isUserNameExsit = True
            else:
                messages.error(request, 'Tên Tài Khoản Chỉ Được Chứa Chữ, Số!')
        # form = UserCreationForm(request.POST)
        if isUserNameExsit and isEmailExsit and isPassword:
            print("thanh cong") 
            print(form.is_valid())
            if form.is_valid():
                print("valid")
                form.save()
                login(request, form)
                return redirect("homepage")

    else:
        pass
        # messages.error(request, 'Có lỗi trong quá trình đăng kí! Vui lòng thử lại sau.')
    return render(request, 'register.html', context)
