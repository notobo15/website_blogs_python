from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path("contact/", views.contact, name="contact"),
    path("aboutus/", views.aboutus, name="aboutus"),
    # path("like-article/", views.like_article, name='like-article'),
    path('create-article/', views.createArticle, name='create-article'),
    path('update-article/<str:id>/', views.updateArticle, name='update-article'),
    path('delete-article/<str:id>/', views.deleteArticle, name='delete-article'),


    path('<str:pk>/', views.category, name='category'),

    path('<str:pk>/<slug:detail>/', views.detail, name='detail'),
    path("<str:pk>/<slug:detail>/like-article/",
         views.like_article, name='like-article'),


]
