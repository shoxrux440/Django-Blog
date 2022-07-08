from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('shop_list', DisplayShopsView.as_view(), name='shop'),
    path('shop_items_list/<int:pk>', DisplayShopItemView.as_view(), name='shop_item'),
    path('ssa', DisplayProductItems.as_view(), name='shop_items')

]

