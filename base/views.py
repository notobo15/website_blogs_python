from .forms import CreateUserForm
from django.shortcuts import render, redirect
from . import models
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import re
from datetime import datetime
from .forms import CreateCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def homepage(request):
    category = models.Category.objects.all()
    posts = models.Article.objects.all()
    context = {"category" : category, "posts" : posts}
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


def detail(request, pk,  detail):
    posts = models.Article.objects.order_by('-created')[:7]
    if models.Article.objects.filter(slug=detail).exists():
        article = models.Article.objects.get(slug=detail)
        allcomments = models.Comment.objects.filter(article=article.id)
        context['allcomments'] = allcomments
        context['article'] = article
        # context['user'] = request.user
        print(allcomments)
        context['comment_form'] = CreateCommentForm()
        
        """ 
        number_page = 20
        print(allcomments[number_page -1].parent)

        while allcomments[number_page - 1].parent != None:
            number_page +=1 
          
         """
        # page = request.GET.get('page', 1)
        # context['page'] = page
        # paginator = Paginator(allcomments, 10)
        # try:
        #     comments = paginator.page(page)
        # except PageNotAnInteger:
        #     comments = paginator.page(1)
        # except EmptyPage:
        #     comments = paginator.page(paginator.num_pages)
        # context['comments'] = comments
    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect("login")
        comment_form = CreateCommentForm(request.POST) 
        if comment_form.is_valid():
            user_comment = comment_form.save(commit = False)
            user_comment.article = article
            user_comment.user = request.user
            user_comment.save()

            allcomments = models.Comment.objects.filter(article=article.id)

            # paginator = Paginator(allcomments, 10)
            # try:
            #     comments = paginator.page(page)
            # except PageNotAnInteger:
            #     comments = paginator.page(1)
            # except EmptyPage:
            #     comments = paginator.page(paginator.num_pages)
            # context['comments'] = comments
            context['allcomments'] = allcomments
            context['comment_form'] = CreateCommentForm()
            # return render(request, 'detail.html', context)

    for com in allcomments:
        current_time = datetime.now()
        # print(current_time)
        year = com.publish.year
        month = com.publish.month
        day = com.publish.day
        hour = com.publish.hour
        minute = com.publish.minute
        second = com.publish.second
        past_time = datetime(year, month, day, hour, minute, second)
        # print("past time : ", past_time)
        time_diff = current_time - past_time
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        days = int(days)
        hours = int(hours)
        minutes = int(minutes)
        # print("Số ngày: ", days)
        # print("Số giờ: ", hours)
        # print("Số phút: ", minutes)
        if hours == 0 and days == 0:
            str = f'{minutes} phút trước'
        elif days == 0:
            str = f'{hours} giờ {minutes} phút trước'
        else:
            str = f'{days} ngày {hours} giờ {minutes} phút trước'
        com.number_time = str
        print(com.number_time)    
    
    context['comment_form'] = comment_form
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


def like_article(request, pk, detail):
    print(request)
    user = request.user
    if request.method == "POST":
        article_id = request.POST.get("article_id")
        article = models.Article.objects.get(id=article_id)
        print(article_id)
        print(article)
        if user in article.liked.all():
            print('da like')
            article.liked.remove(user)
        else:
            article.liked.add(user)
        like, created = models.Like.objects.get_or_create(user=user, article_id=article_id)
        print(like.value)
        print(created)

        if not created:
            if like.value == "Like":
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        print(like.value)
        like.save()
        return redirect(f'../../../{pk}/{detail}')
        # return redirect(f'homepage')