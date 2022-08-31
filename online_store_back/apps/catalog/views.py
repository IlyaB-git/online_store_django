from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Category, Product, Vendor
from .utils import CategoriesList


class IndexView(CategoriesList, ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'catalog_products_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | self.get_extra_context(title='Интернет магазин')

    def get_queryset(self):
        return self.model.objects.filter(is_public=True)


class CategoryView(IndexView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | self.get_extra_context(
            title=get_object_or_404(Category, slug=self.kwargs['category_slug']).name)

    def get_queryset(self):
        return self.model.objects.filter(category__slug=self.kwargs['category_slug'], is_public=True)


class VendorView(IndexView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | self.get_extra_context(title=get_object_or_404(Vendor, slug=self.kwargs['vendor_slug']).name)

    def get_queryset(self):
        return self.model.objects.filter(vendor__slug=self.kwargs['vendor_slug'], is_public=True)


class ProductView(CategoriesList, DetailView):
    model = Product
    template_name = "product.html"
    pk_url_kwarg = "product_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | self.get_extra_context(title=context['product'],
                                                add_to_cart=self.request.GET.get('add_to_cart'))


class SearchView(IndexView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | self.get_extra_context(search_text=self.request.GET.get('text'))

    def get_queryset(self):
        return self.model.objects.filter(name__icontains=self.request.GET.get('text'), is_public=True)
