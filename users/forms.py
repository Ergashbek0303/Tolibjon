from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username', widget=forms.TextInput(attrs={
        'class':'input100'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input100'
    }))
    class Meta:
        models=User
        fields=('username','password')




class UserRegistrationForm(UserCreationForm):
    firstname=forms.CharField(label='Firsname', widget=forms.TextInput(attrs={
        'placeholder':'Enter your firstname'
    }))
    lastname=forms.CharField(label='Lastname', widget=forms.TextInput(attrs={
        'placeholder':'Enter your lastname'
    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your username'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your email'
    }))
    password1=forms.CharField( widget=forms.PasswordInput(attrs={
        'placeholder':'Create new password'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm your password'
    }))

    class Meta:
        model=User
        fields=('firstname','lastname','username','email','password1','password2')