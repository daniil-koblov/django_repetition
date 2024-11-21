from django.urls import path
from . import views
from .views import year_post, MonthPost, post_detail, HelloView, TemplIf, view_for
from .views import index, about


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('HelloView/', views.HelloView.as_view(), name='HelloView'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('my_view/', views.my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
]
