from django.urls import path
from .views import OrderCreateView, OrderView, OrderListView

urlpatterns = [
    path('createorder/', OrderCreateView.as_view(), name='order_create'),
    path('<int:order_id>/', OrderView.as_view(), name='order'),
    path('', OrderListView.as_view(), name='order_list')
]