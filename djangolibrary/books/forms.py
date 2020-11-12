from django.forms import ModelForm
from django import forms
from . import models

class CreateBook(ModelForm):
    class Meta:
        model = models.Book
        fields = ['title','ISBN','author','cover']


class EditBook(ModelForm):
    class Meta:
        model = models.Book
        fields = ['title','ISBN','author','cover']
