from django.urls import path
from .views import IndexView, CategoryView, ProductView, SearchView,VendorView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<str:category_slug>', CategoryView.as_view(), name='category'),
    path('search/', SearchView.as_view(), name='search'),
    path('product/<int:product_id>', ProductView.as_view(), name='product'),
    path('vendor/<str:vendor_slug>', VendorView.as_view(), name='vendor'),
]