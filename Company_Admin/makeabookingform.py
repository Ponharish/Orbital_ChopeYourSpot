from django import forms
from django.core.exceptions import ValidationError
from login.models import users
from login.models import registeredDomains
from .models import ListOfCommonSpaces

class DateInput(forms.DateInput):
    input_type = 'date'

class makeabookingform(forms.Form):
    username = forms.CharField(
        max_length=30, 
        label="Username", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'John'})
        )
    placeid = forms.IntegerField(
        label='ID',
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': '15'
        })
    )

    booking_date = forms.DateField(
        required=False,
        widget=DateInput(attrs={'type': 'date'})
    )

    start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    
    end_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))

