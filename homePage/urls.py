from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name = 'homePage'),
    path('feedback', views.feedback, name = 'feedback'),
    path('feedback_thank_you', views.feedback_thank_you, name='feedback_thank_you'),
    path('enquiry', views.enquiry, name = 'enquiry'),
    path('enquiry_ack', views.enquiry_ack, name='enquiry_ack'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('searchforcompanies', views.searchforcompanies, name = 'searchforcompanies'),
]