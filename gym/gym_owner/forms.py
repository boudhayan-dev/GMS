from django.forms import ModelForm, PasswordInput
from django import forms
from .models import Owner, Address, Gym
from django.contrib.auth.models import User

# Custom Login Form
from django.contrib.auth.forms import AuthenticationForm, UsernameField
# Date-time widget picker
from django.contrib.admin import widgets


class UserForm(ModelForm):
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        # fields =  ('username','first_name','last_name','email','password')
        fields = ('password',)
        # fields =  '__all__'


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        # fields = ('gym', 'address', 'contact', 'aadhar', 'pan', 'gender',  'profile_photo')
        # fields = ('first_name', 'last_name', 'email', 'gym', 'contact', 'aadhar', 'pan', 'gender',  'profile_photo')
        fields = ('first_name', 'last_name', 'email',
                  'contact', 'aadhar', 'pan', 'gender', 'profile_photo')


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('building', 'street', 'city', 'state', 'country')


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class GymForm(ModelForm):
    class Meta:
        model = Gym
        fields = ('name', 'contact', 'gst_number', 'email')
