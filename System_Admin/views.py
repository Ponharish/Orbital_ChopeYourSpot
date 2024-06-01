from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def System_Admin_Dashboard(request): #OK
    first_name = request.session['Current_login_data']['first_name']
    return render(request, 'System_Admin_Dashboard.html', {'first_name': first_name})