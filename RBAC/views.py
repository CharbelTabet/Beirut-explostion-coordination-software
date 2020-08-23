from django.shortcuts import render
from django.views.generic import TemplateView

class login(TemplateView):
    template_name = 'auth/login.html'

class register(TemplateView):
    template_name = 'auth/register.html'

class forgot(TemplateView):
    template_name = 'auth/forgot.html'
