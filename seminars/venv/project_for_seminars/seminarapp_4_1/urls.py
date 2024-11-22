from .views import index, games, add_author, add_article, articles
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('games/', games, name='games'),
    path('author/', add_author, name='add_author'),
    path('add_article/', add_article, name='add_article'),
    path('articles/', articles, name='articles'),
]
