from django.shortcuts import render,get_object_or_404
from .models import ShopVariety
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    typeshop = ShopVariety.objects.all()  # Fetch all shop data
    return render(request, 'shops\home.html', {'typeshop': typeshop})

def detail(request,detail_id):
    shop = get_object_or_404(ShopVariety,pk=detail_id)
    return render(request, 'shops/detail.html', {'shop':shop})