from django.urls import path
from . import views




urlpatterns = [ 
    path('', views.homepage, name='homepage'),
    path('create-article/', views.createArticle, name='create-article'),

    
    path('<str:pk>/', views.category, name='category'),

    path('<str:pk>/<str:detail>/', views.detail, name='detail'),


]