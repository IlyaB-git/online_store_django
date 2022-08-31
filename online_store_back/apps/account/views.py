from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView


class AccountLoginView(LoginView):
    template_name = 'login.html'
    # redirect_field_name = '/'
    # redirect_authenticated_user = '/'


class AccountLogoutView(LogoutView):
    template_name = 'logout.html'


def d(request):
    return HttpResponse('prof')
