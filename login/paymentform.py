from django import forms
from django.core.exceptions import ValidationError
from .models import users, registeredDomains, payments

class PaymentForm(forms.Form):
    PaymentReference = forms.CharField(
        max_length=30, 
        label="Payment Reference", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'ABCD1234'})
        )
