from django.contrib import admin
from django.urls import path, include
from .  import views
app_name = 'post_mail'
urlpatterns = [
    path('', views.show_mypage, name='show_mypage'),
    path('add_guest', views.add_guest, name='add_guest'),
]
