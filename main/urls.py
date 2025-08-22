from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('folder/<str:folder_name>/', views.folder_view, name='folder'),
    path('media/<int:file_id>/', views.player_view, name='player'),
]
