from django import forms
from django.core.exceptions import ValidationError
from .models import users
from .models import registeredDomains

class newpasswordform(forms.Form):



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

    


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        

        errors = {}

        if password and confirm_password:
            
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