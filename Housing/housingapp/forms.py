from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *






class CustomUserCreationForm(UserCreationForm):
    # Add custom fields or modify existing ones here
    class Meta:
        model = User  # Replace 'User' with your custom user model if necessary
        fields = ['username', 'email', 'password1', 'password2']

class SearchForm(forms.Form):
    # developer_name=forms.CharField(max_length=255,required=False)
    # city=forms.CharField(max_length=255,required=False)
    query=forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'on'}))


class FlatmateChoiceForm(forms.Form):
    FLATMATE_CHOICES = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        ('Food Available', 'Food Available'),
        ('Private Room', 'Private Room'),
    ]

    flatmate_choice = forms.ChoiceField(
        choices=FLATMATE_CHOICES,
        widget=forms.RadioSelect,
        initial='Boys',  # Set the default choice if needed
    )

class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model=User
        fields=('username','email','password1','password2','is_user','is_agent','is_owner','is_builder','is_flatmate','is_staff')