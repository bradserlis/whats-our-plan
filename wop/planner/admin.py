from django.contrib import admin

# Register your models here.

from .models import Group, Profile

admin.site.register(Group)
admin.site.register(Profile)

