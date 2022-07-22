from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('actual/', views.actual, name='actual'),
    path('newest/', views.newest, name='newest'),
    path('news/', views.news, name='news'),
    path('show/', views.show, name='show'),
    path('sport/', views.sport, name='sport'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('tech/', views.tech, name='tech'),
    path('viral/', views.viral, name='viral'),
    path('search_result/', views.search_result, name='search-result'),

   
]