from django.urls import path
from . import views

urlpatterns = [
    path('queryset_test/', views.queryset_test),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('basket/', views.basket, name='basket'),
    path('menu/', views.menu, name='menu'),
    path('', views.sign_up_by_html, name='registration'),
]
