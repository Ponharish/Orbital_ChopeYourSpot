from django import forms
from django.core.exceptions import ValidationError
from login.models import users
from login.models import registeredDomains
from .models import ListOfCommonSpaces


class addcommonspaceform(forms.Form):
    space_name = forms.CharField(
        max_length=30, 
        label="Space Name", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'L3 Meeting Room'})
        )

    description = forms.CharField(
        max_length=50, 
        label="description", 
        required=True,
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 30, 'placeholder': 'Description of place', 'style': 'resize:none; height: 150px;'})
    )

    location = forms.CharField(
        max_length=50, 
        label="location", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Level 3 room 2'})
    )

    capacity = forms.IntegerField(
        label='Capacity',
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': '15'
        })
    )


    #Add all individual day availability here


    available_monday = forms.BooleanField(required=False)
    monday_start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    monday_end_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))

    available_tuesday = forms.BooleanField(required=False)
    tuesday_start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    tuesday_end_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))


    available_wednesday = forms.BooleanField(required=False)
    wednesday_start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    wednesday_end_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))

    available_thursday = forms.BooleanField(required=False)
    thursday_start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    thursday_end_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))

    available_friday = forms.BooleanField(required=False)
    friday_start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    friday_end_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))

    available_saturday = forms.BooleanField(required=False)
    saturday_start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    saturday_end_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))

    available_sunday = forms.BooleanField(required=False)
    sunday_start_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))
    sunday_end_time = forms.TimeField(required=False,widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}))

    #IF a day is selected and time is not given, catch it in the form evaluation and raise error!!
    #and also evaluate time to make sure that the given timing does notexceed the day
    #remove step of 30 mins if req




    ReservationRestrictions = forms.CharField(
        max_length=50, 
        label="Reservation Restrictions", 
        required=False,
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 30, 'placeholder': 'Any restrictions on reserving the place', 'style': 'resize:none; height: 150px;'})
    )

    AdditionalFeatures = forms.CharField(
        max_length=50, 
        label="Additional Features", 
        required=False,
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 30, 'placeholder': 'Any additional information/features of this place', 'style': 'resize:none; height: 150px;'})
    )

 

    def clean_domain(self):
        domain = self.cleaned_data.get('domain').strip()
        if domain[0] != '@':
            raise ValidationError("Invalid Domain")
        
        return domain


    def clean(self):
        errors = {}
        cleaned_data = super().clean()
        capacity = cleaned_data.get('capacity')
        if capacity <= 0:
            errors['capacity'] = 'Invalid value entered for location capacity'
        # domain = cleaned_data.get('domain')
        # space_name = cleaned_data.get('space_name')

        # place = ListOfCommonSpaces.objects.filter(space_name=space_name, domain = domain).exists()
        # if place:
        #     errors['space_name'] = "Place already exists"

        ################################################################
        ################################################################
        ## DO THIS EVALUATION FROM views.py                           ##
        ## Dont take domain from user, extract it from session cookie ##
        ################################################################
        ################################################################

        
        if errors:
            raise ValidationError(errors)

        return cleaned_data