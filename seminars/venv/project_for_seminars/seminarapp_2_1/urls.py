from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coin_flip/', views.flip_coin_view, name='coin_flip'),
]
