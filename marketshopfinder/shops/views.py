from django.shortcuts import render,get_object_or_404
from .models import ShopVariety
from django.shortcuts import HttpResponse
from django.template.loader import get_template

# Create your views here.
def home(request):
    typeshop = ShopVariety.objects.all()  # Fetch all shop data
    return render(request, 'home.html', {'typeshop': typeshop})
