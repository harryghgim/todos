from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import CustomUser

# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)