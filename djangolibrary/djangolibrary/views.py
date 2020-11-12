from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html', {'title': 'Home Page'})

def about(request):
    return render(request, 'about.html', {'title': 'About Page'})
    # return HttpResponse('about')