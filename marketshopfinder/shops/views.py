from django.shortcuts import render,get_object_or_404
from .models import ShopVariety,Store
from django.shortcuts import HttpResponse
from .forms import ShopVarietyForm

# Create your views here.
def home(request):
    typeshop = ShopVariety.objects.all()  # Fetch all shop data
    return render(request, 'shops\home.html', {'typeshop': typeshop})

def detail(request,detail_id):
    shop = get_object_or_404(ShopVariety,pk=detail_id)
    return render(request, 'shops/detail.html', {'shop':shop})

def shop_store_view(request):
    stores=None
    if request.method == 'POST':
        form = ShopVarietyForm(request.POST)
        if form.is_valid():
            shop_variety=form.cleaned_data['shop_variety']
            stores=Store.objects.filter(shopvarities=shop_variety)
    else:
        form=ShopVarietyForm()
    return render(request,'shops/shopstores.html',{'form':form,'stores':stores})
