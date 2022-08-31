from django.urls import path
from .views import CartView, CartAddView, CartRemoveView, CartUpdateView

urlpatterns = [
    path('add/', CartAddView.as_view(), name='cart_add'),
    path('remove/', CartRemoveView.as_view(), name='cart_remove'),
    path('update/', CartUpdateView.as_view(), name='cart_update'),
    path('', CartView.as_view(), name='cart'),
]