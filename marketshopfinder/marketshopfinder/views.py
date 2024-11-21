from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'layout.html')

def About(request):
    return HttpResponse("<h1>Welcome To: About</h1>")

def Contact(request):
    return HttpResponse("<h1>Welcome To: Contact</h1>")