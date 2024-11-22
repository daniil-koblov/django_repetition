from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'register_date']
    ordering = ['name', 'register_date']
    list_filter = ['email', 'register_date']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя клиента (name)'

    readonly_fields = ['register_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контакты',
            {
                'classes': ['collapse'],
                'fields': ['email', 'phone', 'address'],
            }
        ),
        (
          'Дата регистрации',
          {
              'classes': ['collapse'],
              'fields': ['register_date'],
          }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'total_amount', 'order_date']
    ordering = ['order_date', 'total_amount', 'buyer']
    list_filter = ['order_date', 'total_amount', 'buyer']
    search_fields = ['buyer__name', 'order_date']
    search_help_text = 'Поиск по полю Имя клиента (buyer__name) и дате заказа (order_date)'

    readonly_fields = ['order_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['buyer'],
            },
        ),
        (
            'Заказ',
            {
                'classes': ['collapse'],
                'fields': ['products', 'total_amount'],
            }
        ),
        (
            'Дата заказа',
            {
                'classes': ['collapse'],
                'fields': ['order_date'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'quantity', 'product_add_date', 'product_image',]
    ordering = ['product_add_date', 'title', 'price']
    list_filter = ['product_add_date', 'title', 'price']
    search_fields = ['title', 'description']
    search_help_text = 'Поиск по полю Название товара (title) и описанию (description)'

    readonly_fields = ['product_add_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title', 'description', 'price', 'quantity'],
            }
        ),
        (
            'Изображение товара',
            {
                'classes': ['collapse'],
                'fields': ['product_image'],
            }
        ),
        (
            'Дата добавления товара',
            {
                'classes': ['collapse'],
                'fields': ['product_add_date'],
            }
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
