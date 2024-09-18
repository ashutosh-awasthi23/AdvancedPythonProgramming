from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, 'myapp/home.html')


def about(request):
    # return HttpResponse("This is about Page!")
    return render(request, 'myapp/about.html')
