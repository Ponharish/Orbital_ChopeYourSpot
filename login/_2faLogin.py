from django import forms
from django.core.exceptions import ValidationError
from .models import users, registeredDomains

class _2faLoginForm(forms.Form):
    OTP = forms.CharField(
        max_length=6, 
        label="OTP", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'OTP'})
        )
