from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "username",
    "email",
    "phone",
    "user_type",
    "is_admin",
    "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("user_type","phone",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("user_type","phone",)}),)
admin.site.register(CustomUser, CustomUserAdmin)
