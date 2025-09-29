from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 rounded-lg border border-pink-300 bg-white/60 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-pink-400',
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 rounded-lg border border-pink-300 bg-white/60 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-pink-400',
        'placeholder': 'Enter your password'
    }))


class CustomRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 rounded-lg border border-pink-300 bg-white/60 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-pink-400',
        'placeholder': 'Enter your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 rounded-lg border border-pink-300 bg-white/60 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-pink-400',
        'placeholder': 'Confirm password'
    }))


    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-pink-300 bg-white/60 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-pink-400',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-pink-300 bg-white/60 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-pink-400',
                'placeholder': 'Enter your email'
            }),
        }