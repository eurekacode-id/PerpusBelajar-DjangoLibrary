from django.contrib import admin
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_index, name='index'),
    path('create/', views.book_create, name='create'),
    path('edit/<int:id>', views.book_edit, name='edit'),
    path('<int:id>', views.book_details, name='details'),
    path('delete/<int:id>', views.book_delete, name='delete'),
]