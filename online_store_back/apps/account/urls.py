from django.urls import path, include
from .views import AccountLoginView, AccountLogoutView

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    # path('profile/', d, name='profile')
    path('logout/', AccountLogoutView.as_view(), name='logout')
    # path('accounts/', include('django.contrib.auth.urls')),
]