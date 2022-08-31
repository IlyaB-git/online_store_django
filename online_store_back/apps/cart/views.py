from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin, DeleteView
from django.views.generic.base import View
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Cart
from catalog.models import Product


class CartView(ListView):
    template_name = 'cart.html'
    model = Cart
    context_object_name = 'cart'


class CartAddView(View):
    def post(self, request):
        if Cart.objects.filter(user=request.user, product=request.POST.get('product')):
            return redirect('/1/')
        new_product_in_cart = Cart(user=request.user, count=request.POST.get('count'),
                                   product=get_object_or_404(Product, pk=request.POST.get('product')))

        try:
            new_product_in_cart.full_clean()
            new_product_in_cart.save()
            return redirect(reverse('product', kwargs={'product_id': request.POST.get('product')}) +
                            '?add_to_cart=success')
        except ValidationError as e:
            print(e)
            return redirect('/2')


class CartRemoveView(View):
    def post(self, request):
        if request.POST.get('action') == 'remove_one':
            Cart.objects.filter(product=request.POST.get('product_id'), user=request.user).delete()
        return redirect(reverse('cart'))


class CartUpdateView(View):
    def post(self, request):
        print(request.POST)
        item = get_object_or_404(Cart, product=request.POST.get('product_id'), user=request.user)
        item.count = request.POST.get('count')
        item.save()
        return redirect(reverse('cart'))
