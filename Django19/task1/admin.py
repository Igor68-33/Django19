from django.contrib import admin
from .models import Buyer, Game, News


# Register your models here.

@admin.register(Buyer)
class Buyer(admin.ModelAdmin):
    list_display = ('username', 'balance', 'age')
    search_fields = ('username',)
    list_filter = ('balance', 'age',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class Buyer(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    search_fields = ('title',)
    list_filter = ('cost', 'size',)
    list_per_page = 20

    # Разбитие по секциям
    fieldsets = (
        (None, {
            'fields': ('title', 'cost', 'size',)
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),   # Скрыть дополнительные поля
            'fields': ('description', 'age_limited',)
        })
    )

@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    search_fields = ('title',)
    list_filter = ('date', )
    list_per_page = 30