from django.shortcuts import render
from .models import *
from django.views.generic import (
    ListView,
    DetailView
)
# Create your views here.


class DisplayShopsView(ListView):
    model = Shop
    template_name = 'shop/shop_list.html'
    context_object_name = 'shops'


class DisplayShopItemView(ListView):
    model = ShopItem
    template_name = 'shop/shop_item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['items'] = ShopItem.objects.filter(shop__id=self.kwargs['pk'])
        return context


class DisplayProductItems(ListView):
    model = ShopItem
    template_name = 'shop/product_items.html'
    context_object_name = 'items'



