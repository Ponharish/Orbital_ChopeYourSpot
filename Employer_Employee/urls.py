from django.urls import path
from . import views


urlpatterns = [
    path('', views.Employer_Employee_Dashboard, name = 'Employer_Employee_Dashboard'),
    path('logoutpageusr', views.logoutpageusr, name = 'logoutpageusr'),
]