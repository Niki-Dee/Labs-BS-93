from django.shortcuts import render


def home(request):
    return render(request, "mainApp/homePage.html")

def about(request):
    return render(request, "mainApp/about.html")

def contact(request):
    return render(request, "mainApp/contact.html")
# Create your views here.
