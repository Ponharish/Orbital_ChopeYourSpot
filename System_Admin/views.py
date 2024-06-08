from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from login.models import registeredDomains
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def System_Admin_Dashboard(request): #OK
    first_name = request.session['Current_login_data']['first_name']
    company = registeredDomains.objects.get(domain = request.session['Current_login_data']['domain'])
    return render(request, 'System_Admin_Dashboard.html', {'first_name': first_name, 'company' : company.company_name})

@never_cache
def logoutpage(request):
    request.session.pop('Current_login_data', None)
    return render(request, 'logoutpage.html')

@never_cache
def viewlistofcompanies(request):
    companies = registeredDomains.objects.all()
    is_empty = not companies.exists()  # Check if queryset is empty
    return render(request, 'viewlistofcompanies.html', {'companies': companies, 'is_empty': is_empty})

@never_cache
def seependingrequest(request):
    companies = registeredDomains.objects.filter(approved=False)
    is_empty = not companies.exists() # Check if queryset is empty
    return render(request, 'seependingrequest.html', {'companies': companies, 'is_empty': is_empty})
