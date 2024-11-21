from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flip_coin/<int:tryes>', views.flip_coin, name='flip_coin'),
    path('random_roll/<int:tryes>', views.random_roll, name='random_roll'),
    path('random_number/<int:tryes>', views.random_number, name='random_number'),
]
