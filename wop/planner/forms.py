from django import forms
from .models import Group

# ===
# App forms
# ===

class GroupCreate(forms.ModelForm):
    class Meta:
        model=Group
        fields=('name', 'description')
        success_url = ''
# class ActivityCreate(forms.ModelForm):
#     class Meta:
#         model=Activity
#         fields = ('title', 'description')

# ===
# Auth
# ===

class SignupForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

