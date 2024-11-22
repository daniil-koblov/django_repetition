from django.contrib import admin
from .models import Author, Article, Comment


@admin.action(description="Сменить имя на None")
def set_name_to_none(modeladmin, request, queryset):
    queryset.update(name='None')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'bio', 'birthday']
    ordering = ['name', 'birthday']
    list_filter = ['email', 'birthday']
    search_fields = ['bio']
    search_help_text = 'Поиск по полю Биография автора (bio)'

    readonly_fields = ['birthday']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Фамилия и биография автора',
                'fields': ['last_name', 'bio'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Дата рождения',
                'fields': ['birthday'],
            }
        ),
    ]


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Author, AuthorAdmin)
