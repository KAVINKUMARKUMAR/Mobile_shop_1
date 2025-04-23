from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
from .form import CustomLogin,CustomRegister
from django.contrib.auth.views import LoginView


class userregister(CreateView):
    form_class = CustomRegister
    template_name = 'signup.html'
    success_url = reverse_lazy('signin')

class userlogin(LoginView):
    form_class = CustomLogin
    template_name  = 'signin.html'