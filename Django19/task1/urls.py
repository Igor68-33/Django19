from django.urls import path
from . import views

urlpatterns = [
    path('queryset_test/', views.queryset_test),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('basket/', views.basket, name='basket'),
    path('news/', views.news, name='news'),
    path('', views.sign_up_by_html, name='registration'),
    path('api/buyers/', views.buyer_list_api, name='buyer_list_api'),  # API для покупателей
    path('api/games/', views.game_list_api, name='game_list_api'),  # API для игр

]
