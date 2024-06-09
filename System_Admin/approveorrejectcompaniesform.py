from django import forms
from django.core.exceptions import ValidationError
from login.models import users
from login.models import registeredDomains

class ApproveOrRejectCompanyForm(forms.Form):

    domain = forms.CharField(
        max_length=30, 
        label="Domain", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '@abc'})
    )


    def clean_domain(self):
        domain = self.cleaned_data.get('domain').strip()
        if domain[0] != '@':
            raise ValidationError("Invalid Domain")
        
        return domain


    def clean(self):
        cleaned_data = super().clean()
        domain = cleaned_data.get('domain')

        errors = {}

        if domain:
            

            company_exists = registeredDomains.objects.filter(domain = domain, approved=False).exists()
            if not company_exists:
                errors['domain'] = "Invalid Domain"
  
        
        if errors:
            raise ValidationError(errors)

        return cleaned_data