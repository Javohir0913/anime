from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Kerakli maydonlar


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
