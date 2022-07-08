from django.contrib import admin
from django.urls import path
from .views import ProductListView, CategoryView, ProductUpdateView, search_venues, SubCategoryView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('subcategory/<str:subcats>', SubCategoryView, name='subcategory'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('search', search_venues, name='search'),

]

urlpatterns += staticfiles_urlpatterns()