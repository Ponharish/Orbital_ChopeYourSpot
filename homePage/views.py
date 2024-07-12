from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .FeedbackForm import FeedbackForm
from .EnquiryForm import EnquiryForm
from .models import Feedback, Enquiry
from login.models import registeredDomains
import smtplib

# Create your views here.

def homePage(request):
    return render(request, 'MainPage.html')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            rating = form.cleaned_data['rating']
            feedback_text = form.cleaned_data['feedback']

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                msg='Dear '+name +',\nThank you for your feedback.'+'\n\nWarm Regards\nChopeYourSpot Team '
                sub='Feedback Received'

                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login('chopeyourspot@gmail.com','ybacagvwwwacqukr')    
                subject = sub
                body = msg
                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail('chopeyourspot@gmail.com',email,msg)


            
            # Save feedback to the database
            feedbackdet = Feedback(name=name, email=email, rating=rating, feedback_text=feedback_text)
            feedbackdet.save()
            

            return redirect('feedback_thank_you')  
    else:
        form = FeedbackForm()

    return render(request, 'FeedbackForm.html', {'form': form})


def feedback_thank_you(request):
    return render(request, 'feedbackThankYou.html')


def enquiry_ack(request):
    return render(request, 'equiryAck.html')

def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Phone = form.cleaned_data['Phone']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            enquirymessage = form.cleaned_data['enquirymessage']
            

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                msg='Dear '+name +',\nWe have received your enquiry on'+subject+'. We would get back to you soon via email/phone.'+'\n\nWarm Regards\nChopeYourSpot Team '
                sub='Enquiry Received'

                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login('chopeyourspot@gmail.com','ybacagvwwwacqukr')    
                subject = sub
                body = msg
                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail('chopeyourspot@gmail.com',email,msg)


            
            # Save feedback to the database
            enquirydet = Enquiry(name=name, email=email,Phone = Phone, subject=subject, enquiry_text=enquirymessage)
            enquirydet.save()
            

            return redirect('enquiry_ack')  
    else:
        form = EnquiryForm()

    return render(request, 'EnquiryForm.html', {'form': form})


def aboutus(request):
    return render(request, 'AboutUs.html')

def searchforcompanies(request):
    companies = registeredDomains.objects.all()
    is_empty = not companies.exists()  # Check if queryset is empty
    return render(request, 'viewlistofcompanieshomepage.html', {'companies': companies, 'is_empty': is_empty})
