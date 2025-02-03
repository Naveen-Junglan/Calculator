from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    data = {
        "title": "AGProperty",
        'heading' : "Hi sir this side naveen singh from ATI "
    }
    return render(request, 'index.html',data)

def aboutUs(request):
    return render(request, 'about-us.html')

def contactUs(request):
    return render(request, 'contact-us.html')

def services(request):
    return render(request, 'service.html')