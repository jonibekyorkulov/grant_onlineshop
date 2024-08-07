from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages


class TestView(TemplateView):
    template_name = 'test.html'

class LoginView(View):
    def get(self, request):
        return render(request, 'page-login-register.html', {})

    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(phone = phone, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfuly")
            return redirect('products:home')
        messages.error(request, "Incorrect passwor or phone")
        return render(request, 'page-login-register.html', {})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.warning(request, "Logout Successfuly")
        return redirect('products:home')