from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'blood_group', 'city', 'profile_pic']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
