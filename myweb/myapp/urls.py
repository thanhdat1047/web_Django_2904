from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_items'),
    path('search/', views.search, name='search'),



]
