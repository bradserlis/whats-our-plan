from django import forms
from .models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ===
# App forms
# ===

class GroupCreate(forms.ModelForm):
    class Meta:
        model=Group
        fields=('name', 'description')
        success_url = '/groups'
        
# class ActivityCreate(forms.ModelForm):
#     class Meta:
#         model=Activity
#         fields = ('title', 'description')

# ===
# Auth
# ===

class SignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=('username', 'password1', 'password2',)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=64)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

