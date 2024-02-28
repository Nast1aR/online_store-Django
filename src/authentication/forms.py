from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class CustomAuthenticationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1','password2']
