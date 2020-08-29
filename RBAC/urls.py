from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login.as_view(), name='login'),
    path('logout', views.Logout, name='logout'),
    path('register', views.register.as_view(), name='register'),
    path('forgot', views.forgot.as_view(), name='forgot'),
    path('testform', views.testForm.as_view()),
]