from django import forms
from .models import ShopVariety

class ShopVarietyForm(forms.Form):
    shop_variety=forms.ModelChoiceField(queryset=ShopVariety.objects.all(),label="Select Shop Variety")