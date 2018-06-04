from django import forms
from .models import Group, Activity

class GroupCreate(forms.ModelForm):
    class Meta:
        model=Group
        fields=('name', 'description')
        success_url = ''
class ActivityCreate(forms.ModelForm):
    class Meta:
        model=Activity
        fields = ('title', 'description')