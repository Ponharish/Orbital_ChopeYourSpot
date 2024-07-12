from django import forms
from django.core.exceptions import ValidationError

class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=50, 
        label="Name", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Bill Jackson'})
        )


    email = forms.EmailField(
        max_length=100,
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'abc@pqr.com'}),
        help_text='Please enter a valid email address'
    )

    RATING_CHOICES = [
        (5, ' * '),
        (4, ' * '),
        (3, ' * '),
        (2, ' * '),
        (1, ' * '),
    ]
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        label='Rating',
        required=True,
        widget=forms.RadioSelect()
    )

    feedback = forms.CharField(
        label='Feedback',
        required=True,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 30, 'placeholder': 'Enter your feedback here...'})
    )



    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        rating = cleaned_data.get('rating')
        feedback = cleaned_data.get('feedback')
        

        errors = {}

        if errors:
            raise ValidationError(errors)

        return cleaned_data