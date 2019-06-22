from django.forms import ModelForm
from django import forms
from .models import Customer
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email'
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('contact', 'aadhar', 'pan', 'gender', 'profile_photo')
        # fields = ('first_name','last_name','email','contact', 'aadhar', 'pan', 'gender', 'profile_photo')