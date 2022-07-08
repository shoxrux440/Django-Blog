from django.shortcuts import render
from django.urls import reverse
from django.http import request

from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Product, Category



# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data()
    #     cat_menu = Category.objects.all()
    #     context['cat_menu'] = cat_menu
    #     return context


def CategoryView(request, cats):
    category_product = Product.objects.filter(category__title=cats.title().replace("-", " "))
    return render(request, 'product/categories.html', {'cats': cats.title().replace("-", " "),
                                                       'category_products': category_product})

def SubCategoryView(request, subcats):
    subcategory_product = Product.objects.filter(subcategory__title=subcats.title().replace("-", " "))
    return render(request, 'product/subcategories.html', {'cats': subcats.title().replace("-", " "),
                                                       'subcategory_products': subcategory_product})


def CategoryListView(request, cats):
    cat_menu_list = Category.objects.filter(category__title=cats.title().replace("-", " "))
    return render(request, 'product/category_list.html', {'cat_menu_list': cat_menu_list})


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse("product_list")


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['search']
        product = Product.objects.filter(title__contains=searched)
    return render(request, 'product/search.html', {'searched': searched, 'prods': product})
