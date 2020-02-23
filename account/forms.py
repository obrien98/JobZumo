from django import forms
from django.forms import TextInput, PasswordInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        widgets = {'username': TextInput(attrs={'class':'form-control'}),
                   'first_name': TextInput(attrs={'class':'form-control'}),
                   'last_name': TextInput(attrs={'class':'form-control'}),
                   'email': TextInput(attrs={'class':'form-control'})
        }
