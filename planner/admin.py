from django.contrib import admin

# Register your models here.

from .models import Activity, Group
admin.site.register(Activity, Group)

