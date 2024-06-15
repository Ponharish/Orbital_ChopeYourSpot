from django import forms
from django.core.exceptions import ValidationError


class removecompanyform(forms.Form):
    idfield = forms.IntegerField(
        label='ID',
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': '15'
        })
    )
