from django import forms
from django.core.exceptions import ValidationError

class EnquiryForm(forms.Form):
    name = forms.CharField(
        max_length=50, 
        label="Name", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Bill Jackson'})
        )

    Phone = forms.IntegerField(
        label='Phone',
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': '81234567'
        })
    )

    email = forms.EmailField(
        max_length=100,
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'abc@pqr.com'}),
        help_text='Please enter a valid email address'
    )

    subject = forms.CharField(
        max_length=70, 
        label="Subject", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enquiry on ...'})
        )

    

    enquirymessage = forms.CharField(
        label='Enquiry',
        required=True,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 30, 'placeholder': 'Enter your Message here...'})
    )



    def clean(self):
        cleaned_data = super().clean()
        errors = {}

        if errors:
            raise ValidationError(errors)

        return cleaned_data