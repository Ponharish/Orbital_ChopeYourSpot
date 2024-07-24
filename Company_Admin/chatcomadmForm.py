from django import forms
from django.core.exceptions import ValidationError
from login.models import users
from login.models import registeredDomains

class chatcomadmForm(forms.Form):
    username = forms.CharField(
        max_length=30, 
        label="Username", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'John'})
        )


    domain = forms.CharField(
        max_length=30, 
        label="Domain", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '@abc'})
    )

    subject = forms.CharField(
        max_length=70, 
        label="Subject", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email about ...'})
        )

    message = forms.CharField(
        label='Enquiry',
        required=True,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 30, 'placeholder': 'Enter your Message here...'})
    )

    def clean_domain(self):
        domain = self.cleaned_data.get('domain').strip()
        if domain[0] != '@':
            raise ValidationError("Invalid Domain")
        
        return domain


    def clean(self):
        cleaned_data = super().clean()
        domain = cleaned_data.get('domain')
        username = cleaned_data.get('username')
        errors = {}

        if domain and username:
            

            company_exists = registeredDomains.objects.filter(domain = domain, approved=True).exists()
            if not company_exists:
                errors['domain'] = "Invalid Domain"

            user_exists = users.objects.filter(username=username, domain = domain).exists()
            if not user_exists:
                errors['username'] = "Invalid recipient"
  
        
        if errors:
            raise ValidationError(errors)

        return cleaned_data