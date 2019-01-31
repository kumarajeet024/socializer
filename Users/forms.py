from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','firstname','password1','password2']
