from django.contrib import admin

# Register your models here.

from .models import Group, Profile, Activity, User_Group

admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Activity)
admin.site.register(User_Group)

