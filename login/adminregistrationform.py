from django import forms
from django.core.exceptions import ValidationError
from .models import users, registeredDomains

class adminRegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, 
        label="First Name", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Bill'})
        )

    last_name = forms.CharField(
        max_length=30, 
        label="Last Name", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Jackson'})
        )

    username = forms.CharField(
        max_length=30, 
        label="Username", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Bill789'})
        )

    domain = forms.CharField(
        max_length=30, 
        label="Domain", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '@pqr'})
    )

    companyName = forms.CharField(
        max_length=30, 
        label="companyName", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'ABC Companies'})
    )

    companyAddress = forms.CharField(
        max_length=50, 
        label="companyAddress", 
        required=True,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 19, 'placeholder': 'Address', 'style': 'resize:none; height: 75px;'})
    )

    email = forms.EmailField(
        max_length=100,
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'abc@pqr.com'}),
        help_text='Please enter a valid email address'
    )

    password = forms.CharField(
        widget=forms.PasswordInput, 
        max_length=100, 
        label="Password", 
        required=True,
        )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput, 
        max_length=100, 
        label="Confirm Password", 
        required=True,
        )

    captcha = forms.CharField(
        max_length=9, 
        label="CAPTCHA", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Captcha'})
        )

    def clean_domain(self):
        domain = self.cleaned_data.get('domain').strip()
        if domain[0] != '@':
            raise ValidationError("Invalid Domain")
        
        return domain

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        domain = cleaned_data.get('domain')
        companyName = cleaned_data.get('companyName')
        companyAddress = cleaned_data.get('companyAddress')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        

        errors = {}

        if companyName and companyAddress and first_name and last_name and username and password and domain and email and confirm_password:
            
            user_exists = users.objects.filter(username=username, domain = domain).exists()
            if user_exists:
                errors['username'] = "Username already taken"
                
            domain_exists = registeredDomains.objects.filter(domain = domain).exists()
            if domain_exists:
                errors['domain'] = "Domain already taken"
    
            countforpasswordcaptletter,countforpasswordsmallletter, countforpasswordnumber=0,0,0 #PASSWORD EVALUATION
            for varia in password:
                if ord(varia) in range(65,91):
                    countforpasswordcaptletter+=1
                elif ord(varia) in range(97,123):
                    countforpasswordsmallletter+=1
                elif ord(varia) in range(48,58):
                    countforpasswordnumber+=1
            if countforpasswordcaptletter==0 or countforpasswordsmallletter == 0 or countforpasswordnumber ==0 or len(password)<8:
                errors['password'] = "Weak Password"
  
            if password != confirm_password: #IF PASSWORD ENTERED MATCHEES WITH THE CONFIRMED ONE
                errors['confirm_password'] = "Passwords do not match"
        
        if errors:
            raise ValidationError(errors)

        return cleaned_data