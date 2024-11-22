from django.contrib import admin
from .models import Author, Article, Comment, Client, Product, Order


admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
