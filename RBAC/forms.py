from django import forms
from django.contrib.auth.models import User

class Register(forms.ModelForm):
    comfirmPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
