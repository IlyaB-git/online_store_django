from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Order, OrderItem
from cart.models import Cart


class OrderView(ListView):
    template_name = 'order.html'
    context_object_name = 'order'
    def get_queryset(self):
        order = get_object_or_404(Order, user=self.request.user, pk=self.kwargs['order_id'])
        queryset = OrderItem.objects.filter(order=order)
        return queryset

class OrderCreateView(View):
    def post(self, request):
        cart = Cart.objects.filter(user=self.request.user)
        if cart:
            price= 0
            for item in cart:
                price += item.product.price * item.product.count
            order = Order.objects.create(user=self.request.user, price=price)
            for item in cart:
                OrderItem.objects.create(product=item.product, order=order, count=item.count)
            cart.delete()
            return redirect(reverse_lazy('order', kwargs={'order_id': order.pk}))
        return redirect(reverse_lazy('cart'))


class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'order_list.html'

