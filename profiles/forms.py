from django import forms
from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']


class RegisterForm(UserCreationForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        "class":"form-control","placeholder":"Enter Username"
    }))
    
    email=forms.CharField(max_length=100,widget=forms.EmailInput(attrs={
        "class":"form-control","placeholder":"Enter Email"
    }))
    
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        "class":"form-control","placeholder":"Enter Password1"
    }))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        "class":"form-control","placeholder":"Enter Password2"
    
    }))
    class Meta:
        model=User
        fields=['username','email','password1','password2']