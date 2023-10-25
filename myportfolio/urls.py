from django.urls import path, include
from . import views


app_name = "myportfolio"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('statistics', views.statistics, name='statistics'),
    path('loginform/', views.loginform, name='loginform')
]
