from django.contrib import admin
from .models import ShopVariety,Shop_review,Store,Cerificate
# Register your models here.


class Shop_reviewInline(admin.TabularInline):
    model=Shop_review
    extra=1

class ShopVarityAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[Shop_reviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('shopvarities',)

class CerificateAdmin(admin.ModelAdmin):
    list_display=('shop','Cnumber','issued_date','valid_until')
    
    
    
admin.site.register(ShopVariety,ShopVarityAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Cerificate,CerificateAdmin)