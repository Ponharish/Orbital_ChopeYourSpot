from django import forms
from django.core.exceptions import ValidationError
from .models import users
from .models import registeredDomains

class PasswordResetOne(forms.Form):
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


    email = forms.EmailField(
        max_length=100,
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'abc@pqr.com'}),
        help_text='Please enter a valid email address'
    )



    def clean_domain(self):
        domain = self.cleaned_data.get('domain').strip()
        if domain[0] != '@':
            raise ValidationError("Invalid Domain")
        
        return domain


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        domain = cleaned_data.get('domain')
        errors = {}

        if username and email and domain:
            

            user_exists = users.objects.filter(username=username, domain = domain).exists()
            if not user_exists:
                errors['username'] = "Incorrect Username or Domain"
            else:
                user = users.objects.get(username=username, domain = domain)
                company = registeredDomains.objects.get(domain = domain)
                if not company.approved:
                    errors['domain'] = "Domain not registered"
                if user.email != email:
                    errors['email'] = "Invalid Email"
        
        if errors:
            raise ValidationError(errors)

        return cleaned_data