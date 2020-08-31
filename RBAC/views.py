from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from . import forms

class Login(View):
    template_name = 'auth/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template_name)
    
    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template_name, {'error_message': 'Credentials did not match', 'username': request.POST.get('username')})

class register(View):
    template_name = 'auth/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/login')
        return render(request, self.template_name)

    def post(self, request):
        newUser = User.objects.create_user(request.POST['username'])
        newUser.email = request.POST['email']
        newUser.set_password(request.POST['password'])
        newUser.first_name = request.POST['first']
        newUser.last_name = request.POST['last']
        newUser.save()
        return HttpResponseRedirect('/')

class forgot(TemplateView):
    template_name = 'auth/forgot.html'

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
