from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from login.models import registeredDomains
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def Company_Admin_Dashboard(request): #OK
    first_name = request.session['Current_login_data']['first_name']
    company = registeredDomains.objects.get(domain = request.session['Current_login_data']['domain'])
    return render(request, 'Company_Admin_Dashboard.html', {'first_name': first_name, 'company' : company.company_name})

@never_cache
def logoutpageca(request):
    request.session.pop('Current_login_data', None)
    return render(request, 'logoutpageca.html')