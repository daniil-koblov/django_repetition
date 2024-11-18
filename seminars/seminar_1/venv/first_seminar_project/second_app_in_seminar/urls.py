from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flip_coin/', views.flip_coin, name='flip_coin'),
    path('random_roll/', views.random_roll, name='random_roll'),
    path('random_number/', views.random_number, name='random_number'),
]
