from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import User


class LoginForm(AuthenticationForm):
    pass

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}