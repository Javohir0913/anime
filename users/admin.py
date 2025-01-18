from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import RegistrationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm
    model = CustomUser
    list_display = ['username', 'email', 'is_active', 'is_staff']
