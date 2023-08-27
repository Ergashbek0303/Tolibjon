from django import forms
from .models import Customers


class CustomersForm(forms.Form):
    name=forms.CharField()
    surname=forms.CharField()
    phone_number=forms.CharField()
    birthday=forms.DateField()
    gender=forms.CharField()
    
