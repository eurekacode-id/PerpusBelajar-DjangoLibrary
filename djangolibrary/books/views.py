from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def book_index(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books/index.html', { 'books': books, 'title': 'Book List'})

@login_required(login_url="/accounts/login/")
def book_create(request):
    if request.method == "POST":
        form = forms.CreateBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:index')
    else:
        form = forms.CreateBook()

    return render(request, 'books/create.html', {'form': form, 'title': 'New Book'})

@login_required(login_url="/accounts/login/")
def book_edit(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = forms.EditBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:index')
    else:
        form = forms.EditBook(instance=book)
    return render(request, 'books/edit.html', {'form': form, 'title': "Edit Book"})

def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/details.html', { 'book': book, 'title': 'Book Details Page'})

def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books:index')

