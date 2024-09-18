from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about_1(request):
    return render(request, "about.html")
