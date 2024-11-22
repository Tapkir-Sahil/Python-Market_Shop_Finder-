from django.shortcuts import render
from .models import ShopVariety

# Create your views here.
def home(request):
    typeshop = ShopVariety.objects.all()  # Fetch all shop data
    return render(request, 'home.html', {'typeshop': typeshop})

# def all_shops(request):
#     typeshop = ShopVariety.objects.all()
#     return render(request, 'shops/templates/home.html',{'typeshop':typeshop})