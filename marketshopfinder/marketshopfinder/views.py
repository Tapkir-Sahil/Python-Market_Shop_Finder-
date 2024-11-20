from django.http import HttpResponse

def Home(request):
    return HttpResponse("<h1>Welcome To: HomePage</h1>")

def About(request):
    return HttpResponse("<h1>Welcome To: About</h1>")

def Contact(request):
    return HttpResponse("<h1>Welcome To: Contact</h1>")