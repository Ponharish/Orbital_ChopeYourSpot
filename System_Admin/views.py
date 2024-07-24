from email import message
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from login.models import registeredDomains
from login.models import users
from login.models import payments
from .models import paymenthistorydump
from django.views.decorators.cache import never_cache
from .approveorrejectcompaniesform import ApproveOrRejectCompanyForm
from .rejectcompanymessageform import rejectcompanymessageform
from .approvecompanymessageform import approvecompanymessageform
from .chatsysadmForm import chatsysadmForm
from.models import Message
import smtplib

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

@never_cache
def approveorrejectcompanies(request):
    if request.method == 'POST':
        form = ApproveOrRejectCompanyForm(request.POST)
        if form.is_valid():

            domain_to_approve = form.cleaned_data.get('domain').strip()    
            request.session['domain_company_data_to_approve'] = domain_to_approve

            return redirect('approveorrejectcompanyinformation')

    else:
        form = ApproveOrRejectCompanyForm()

    return render(request, 'approveorrejectcompanies.html', {
        'form': form,
    })    

@never_cache
def approveorrejectcompanyinformation(request):
    domain_to_approve = request.session.get('domain_company_data_to_approve')
    
    adminoffier = users.objects.filter(domain = domain_to_approve).last()
    company = registeredDomains.objects.filter(domain = domain_to_approve).last()
    paymentinfo = payments.objects.filter(domain = domain_to_approve).last()

    company_details = {
        'company_name':company.company_name,
        'company_Address':company.company_Address,
        'domain':domain_to_approve,
        'first_name':adminoffier.first_name,
        'last_name':adminoffier.last_name,
        'Username':adminoffier.username,
        'email':adminoffier.email,
        'paymentreference':paymentinfo.PaymentReference

    }
    return render(request, 'approveorrejectcompanyinformation.html', {
        'company_details': company_details,
    }) 

@never_cache
def rejectcompanymessage(request):
    msg = request.session['message_given']
    if msg:
        content = msg
    else:
        content = "NIL"

    #SEND EMAIL HERE
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        domain_to_approve = request.session.get('domain_company_data_to_approve')
        adminoffier = users.objects.filter(domain = domain_to_approve).last()
        email = adminoffier.email
        
        msg='Dear '+str(adminoffier.first_name)+',\nWe have processed your request to register your company but regret to inform you that the application outcome is unsuccessful.\n\n Message from System Admin:\n'+content+'\nA full refund will be made to your account in 3 working days.\nif you have any further queries contact us at chopeyourspot@gmail.com' +'\n\nWarm Regards\nChopeYourSpot Team '
        sub='Company Registration Outcome'

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('chopeyourspot@gmail.com','ybacagvwwwacqukr')    
        subject = sub
        body = msg
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail('chopeyourspot@gmail.com',email,msg)

        #UPDATE DB HERE
        company = registeredDomains.objects.filter(domain = domain_to_approve).last()
        paymentinfo = payments.objects.filter(domain = domain_to_approve).last()

        paymentdet = paymenthistorydump(domain = domain_to_approve, PaymentReference = paymentinfo.PaymentReference)
        paymentdet.save()

        paymentinfo.delete()
        company.delete()
        adminoffier.delete()



        #DELETE ALL SESSION COOKIES
        request.session.pop('domain_company_data_to_approve',None)
        request.session.pop('message_given',None)

    return render(request, 'rejectedmessage.html')

@never_cache
def approvecompanymessage(request):
    msg = request.session['message_given']
    if msg:
        content = msg
    else:
        content = "NIL"

    #SEND EMAIL HERE
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        domain_to_approve = request.session.get('domain_company_data_to_approve')
        adminoffier = users.objects.filter(domain = domain_to_approve).last()
        email = adminoffier.email
        msg='Dear '+str(adminoffier.first_name)+',\nWe have processed your request to register your company and happy to inform you that the application outcome is successful.\n\n Message from System Admin:\n'+content+'\n\nYou may be able to log in to the system to add common spaces in your office and the users in your company would be also able to create an account for themselves using the domain name to book and manage\n\n'+'if you have any further queries contact us at chopeyourspot@gmail.com' +'\n\nWarm Regards\nChopeYourSpot Team '
        sub='Company Registration Outcome'

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('chopeyourspot@gmail.com','ybacagvwwwacqukr')    
        subject = sub
        body = msg
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail('chopeyourspot@gmail.com',email,msg)


        #UPDATE DB HERE

        company = registeredDomains.objects.filter(domain = domain_to_approve).last()
        paymentinfo = payments.objects.filter(domain = domain_to_approve).last()

        paymentdet = paymenthistorydump(domain = domain_to_approve, PaymentReference = paymentinfo.PaymentReference)
        paymentdet.save()
        paymentinfo.delete()

        company.approved = True
        company.save()

        #DELETE ALL SESSION COOKIES

        request.session.pop('domain_company_data_to_approve',None)
        request.session.pop('message_given',None)

    return render(request, 'approvedmessage.html')

@never_cache
def rejectcompanymessagetoask(request):
    if request.method == 'POST':
        form = rejectcompanymessageform(request.POST)
        if form.is_valid():

            message = form.cleaned_data.get('Message').strip()    
            request.session['message_given'] = message

            #DELETE THIS COOKIE LATER!!!
            return redirect('rejectcompanymessage')

    else:
        form = rejectcompanymessageform()

    return render(request, 'rejectcompanymessagetoask.html', {
        'form': form,
    })   

@never_cache
def approvecompanymessagetoask(request):
    if request.method == 'POST':
        form = approvecompanymessageform(request.POST)
        if form.is_valid():

            message = form.cleaned_data.get('Message').strip()    
            request.session['message_given'] = message

            #DELETE THIS COOKIE LATER!!!
            return redirect('approvecompanymessage')

    else:
        form = approvecompanymessageform()

    return render(request, 'approvecompanymessagetoask.html', {
        'form': form,
    })   




#CHAT FUNCTIONALITIES
@never_cache
def sysadminbox(request):
    
    messages = Message.objects.filter(receiver=request.session['Current_login_data']['username'], receiverdomain = request.session['Current_login_data']['domain'])
    is_empty = not messages.exists() # Check if queryset is empty
    return render(request, 'sysadminbox.html', {'messages': messages, 'is_empty': is_empty})

def sysadmsent(request):
    messages = Message.objects.filter(sender=request.session['Current_login_data']['username'], senderdomain = request.session['Current_login_data']['domain'])
    is_empty = not messages.exists() # Check if queryset is empty
    return render(request, 'sysadmsent.html', {'messages': messages, 'is_empty': is_empty})


def sysadmcompose(request):
    if request.method == 'POST':
        form = chatsysadmForm(request.POST)
        if form.is_valid():
            sender = request.session['Current_login_data']['username']
            senderdomain = request.session['Current_login_data']['domain']
            receiver = form.cleaned_data.get('username').strip()  
            receiverdomain = form.cleaned_data.get('domain').strip()  
            subject = form.cleaned_data.get('subject').strip()    
            message = form.cleaned_data.get('message').strip()    

            # print(sender)
            # print(senderdomain)
            # print(receiver)
            # print(receiverdomain)
            # print(subject)
            # print(message)

            mailsetails = Message(sender = sender, senderdomain = senderdomain, receiver = receiver, receiverdomain =receiverdomain, subject = subject, content = message)
            mailsetails.save()

            return redirect('sysadmsentack')



    else:
        form = chatsysadmForm()

    return render(request, 'chatcomposesysadm.html', {
        'form': form,
    })   

def sysadmsentack(request):
    return render(request, 'mailcomposesuccesssysadm.html')

def viewlistofusers(request):
    user = users.objects.all()
    is_empty = not user.exists()  # Check if queryset is empty
    return render(request, 'viewlistofusers.html', {'users': user, 'is_empty': is_empty})