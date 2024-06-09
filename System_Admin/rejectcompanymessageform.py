from django import forms
from django.core.exceptions import ValidationError
from login.models import users
from login.models import registeredDomains

class rejectcompanymessageform(forms.Form):


    Message = forms.CharField(
        max_length=100, 
        label="Message", 
        required=False,
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 30, 'placeholder': 'Message (if any)', 'style': 'resize:none; height: 150px;'})
    )


    def clean(self):
        cleaned_data = super().clean()
        message = cleaned_data.get('Message')
        errors = {}
        
        #STORE MESSAGE IN SESSION COOKIE
        
        if errors:
            raise ValidationError(errors)

        return cleaned_data