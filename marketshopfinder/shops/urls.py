from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:detail_id>/',views.detail,name='detail'),
    path('shopstores/',views.shop_store_view,name='shopstores')
]