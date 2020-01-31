from django.contrib import admin
from django.urls import path, include
from .  import views

app_name = 'recommend'

urlpatterns = [
    path('', views.information, name='information'),
    path('add_user/<int:id>/', views.add_user, name='add_user'),
    path('add_more_information/<int:id>/', views.add_more_information, name='add_more_information'),
]
