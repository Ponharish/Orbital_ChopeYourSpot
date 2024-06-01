from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .loginform import LoginForm
from .userregisterform import userRegisterForm
from .adminregistrationform import adminRegisterForm
from ._2faLogin import _2faLoginForm
from ._2faRegister import _2faRegisterForm
from .paymentform import PaymentForm
from .models import users
from .models import registeredDomains
from .models import payments
import random
import logging
import smtplib

######################
## HELPER FUNCTIONS ##
######################
CAPTCHA_DICT = {
    'captcha 1.png': '28ivw',
    'captcha 2.png': 'k4ez',
    'captcha 3.png': '4D7YS',
    'captcha 4.png': '6ne3',
    'captcha 5.png': 'e5hb',
    'captcha 6.png': 'FH2DE',
    'captcha 7.png': 'xmqki',
    'captcha 8.png': '6H3T8',
    'captcha 9.png': 'RBSKW',
}

def select_random_captcha():
    return random.choice(list(CAPTCHA_DICT.items()))

def generate_captcha(request):
    captcha_image, correct_captcha = select_random_captcha()
    request.session['captcha_image'] = captcha_image
    request.session['correct_captcha'] = correct_captcha
    request.session['CaptchaGenerated'] = True



def createAccount(request): #OK
    return render(request, 'Register.html')

def resetPassword(request): #OK for Now
    return render(request, 'resetPassword.html')
  
def handle_redirect_register(request): #ok
    if request.method == 'GET':
        choice = request.GET.get('userType')
        
        if choice == 'Employer_Employee':
            return redirect('registerUser')
        elif choice == 'Company_Admin':
            return redirect('registerAdmin')
        else:
            return HttpResponse(404) 

def usersuccess(request): #OK
    return render(request, 'useraccountcreationmessage.html')
    

def adminsuccess(request): #OK
    return render(request, 'adminaccountcreationmessage.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        correct_captcha = request.session.get('correct_captcha')
        
        if form.is_valid():
            
            if form.cleaned_data['captcha'] == correct_captcha:
                user = users.objects.get(username=form.cleaned_data.get('username').strip(), domain = form.cleaned_data.get('domain').strip())
                Current_login_data = {
                    'first_name' : user.first_name, 
                    'last_name' : user.last_name, 
                    'username' : form.cleaned_data.get('username').strip(), 
                    'domain' : form.cleaned_data.get('domain').strip(), 
                    'email' : user.email,
                    'user_Type' : user.user_Type,
                    }
                
                
                request.session['Current_login_data'] = Current_login_data
                del request.session['CaptchaGenerated']
                del request.session['correct_captcha']
                del request.session['captcha_image']
                request.session['OTP_generated'] = False
                
                return redirect('2falogin')
            else:
                form.add_error('captcha', 'Incorrect Captcha')
                
                generate_captcha(request)
        else:
            generate_captcha(request)
    else:
        form = LoginForm()
        if not request.session.get('CaptchaGenerated'):
            generate_captcha(request)

    corrcapt =request.session['captcha_image']
    return render(request, 'LoginPage.html', {
        'form': form,
        'captcha_image_url': f'/static/captchas/{corrcapt}'
    })

def userRegister_view(request): #FIX BUGS WITH OTP AND CAPTCHA -- OK!
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        correct_captcha = request.session.get('correct_captcha')
        
        if form.is_valid():
            
            if form.cleaned_data['captcha'] == correct_captcha:

                login_data = {
                    'first_name' : form.cleaned_data.get('first_name').strip(), 
                    'last_name' : form.cleaned_data.get('last_name').strip(), 
                    'username' : form.cleaned_data.get('username').strip(), 
                    'domain' : form.cleaned_data.get('domain').strip(), 
                    'password' : form.cleaned_data.get('password').strip(), 
                    'email' : form.cleaned_data.get('email').strip(),
                    'user_Type' : 'Employer/Employee'
                    }
                
                del request.session['CaptchaGenerated']
                del request.session['correct_captcha']
                del request.session['captcha_image']
                request.session['login_data'] = login_data
                request.session['OTP_generated'] = False
                return redirect('2faregister')
            else:
                form.add_error('captcha', 'Incorrect Captcha')
                generate_captcha(request)
        else:
            generate_captcha(request)
    else:
        form = userRegisterForm()
        if not request.session.get('CaptchaGenerated'):
            generate_captcha(request)
    corrcapt =request.session['captcha_image']
    return render(request, 'Registrationformforuser.html', {
        'form': form,
        'captcha_image_url': f'/static/captchas/{corrcapt}'
    })

def AdminRegister_view(request): #FIX BUGS WITH OTP AND CAPTCHA --OK!
    if request.method == 'POST':
        form = adminRegisterForm(request.POST)
        correct_captcha = request.session.get('correct_captcha')
        if form.is_valid():
            
            if form.cleaned_data['captcha'] == correct_captcha:

                login_data = {
                    'first_name' : form.cleaned_data.get('first_name').strip(), 
                    'last_name' : form.cleaned_data.get('last_name').strip(), 
                    'username' : form.cleaned_data.get('username').strip(), 
                    'domain' : form.cleaned_data.get('domain').strip(), 
                    'password' : form.cleaned_data.get('password').strip(), 
                    'email' : form.cleaned_data.get('email').strip(),
                    'user_Type' : 'Company Admin'
                    }
                company_data = {
                    'company_name' : form.cleaned_data.get('companyName').strip(), 
                    'company_Address' : form.cleaned_data.get('companyAddress').strip(), 
                    'admin_officer' : form.cleaned_data.get('username').strip(), 
                    'domain' : form.cleaned_data.get('domain').strip(), 
                    'approved' : False
                }
                
                request.session['login_data'] = login_data
                request.session['company_data'] = company_data
                del request.session['CaptchaGenerated']
                del request.session['correct_captcha']
                del request.session['captcha_image']
                return redirect('payment')
            else:
                form.add_error('captcha', 'Incorrect Captcha')
                generate_captcha(request)
        else:
            generate_captcha(request)
    else:
        form = adminRegisterForm()
        if not request.session.get('CaptchaGenerated'):
            generate_captcha(request)
    corrcapt =request.session['captcha_image']
    return render(request, 'Registrationformforcompanyadmin.html', {
        'form': form,
        'captcha_image_url': f'/static/captchas/{corrcapt}'
    })    

def _2faLogin_view(request): 
    Current_login_data = request.session.get('Current_login_data')
    
    if not Current_login_data:
        return redirect('.')
        
    if request.method == 'POST':
        form = _2faLoginForm(request.POST)
        correct_OTP = request.session.get('correct_OTP')
        if form.is_valid():
            if str(form.cleaned_data['OTP']) == str(correct_OTP):
                del request.session['correct_OTP']
                del request.session['OTP_generated']

                if Current_login_data['user_Type'] == 'Employer/Employee':
                    return redirect('../Employer_Employee') 
                elif Current_login_data['user_Type'] == 'System Admin':
                    return redirect('../System_Admin') 
                elif Current_login_data['user_Type'] == 'Company Admin':
                    return redirect('../Company_Admin') 
                else :
                    return redirect(404)
                ######## CHANGE THE ABOVE LATER WHEN NEW APP IS CREATED!!! ########
            else:
                form.add_error('OTP', 'Incorrect OTP')
                
    else:
        form = _2faLoginForm()
        print(request.session.get('OTP_generated'))
        if not request.session.get('OTP_generated'):

            ##SEND OTP##
            correct_OTP = random.randint(100000,999999)

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                email = Current_login_data['email']
                msg='Dear '+str(Current_login_data['first_name'])+',\nThe OTP is '+str(correct_OTP)+'\n\nWarm Regards\nChopeYourSpot Team '
                sub='OTP Verification'

                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login('chopeyourspot@gmail.com','ybacagvwwwacqukr')    
                subject = sub
                body = msg
                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail('chopeyourspot@gmail.com',email,msg)
            ##     ###

            request.session['correct_OTP'] = correct_OTP
            request.session['OTP_generated'] = True

    return render(request, '2faLogin.html', {
        'form': form
    })    

def _2faRegister_view(request): #FIX BUGS WITH OTP AND CAPTCHA --OK!
    Current_login_data = request.session.get('login_data')

    if not Current_login_data:
        return redirect('.')
    
    if request.method == 'POST':
        form = _2faRegisterForm(request.POST)
        correct_OTP = request.session.get('correct_OTP')
        if form.is_valid():
            if str(form.cleaned_data['OTP']) == str(correct_OTP):
                del request.session['correct_OTP']
                del request.session['OTP_generated']
                ### DO THE SAVING TO DB HERE###

                first_name = Current_login_data['first_name']
                last_name = Current_login_data['last_name']
                username = Current_login_data['username']
                domain = Current_login_data['domain']
                password = Current_login_data['password']
                email = Current_login_data['email']
                user_Type = Current_login_data['user_Type']

                logindet = users(first_name = first_name, last_name = last_name, username = username, domain = domain, password = password, email = email, user_Type = user_Type)
                logindet.save()


                ### maybe move this to the next page!!!
                del request.session['login_data']

                #########################
                return redirect('usersuccess') 
                
            else:
                form.add_error('OTP', 'Incorrect OTP')
                
    else:
        form = _2faRegisterForm()
        if not request.session.get('OTP_generated'):
            ##SEND OTP##
            correct_OTP = random.randint(100000,999999)
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    email = Current_login_data['email']
                    msg='Dear '+str(Current_login_data['first_name'])+',\nThe One Time Password to verify your email is '+str(correct_OTP)+'\n\nWarm Regards\nChopeYourSpot Team '
                    sub='OTP Verification'

                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login('chopeyourspot@gmail.com','ybacagvwwwacqukr')    
                    subject = sub
                    body = msg
                    msg = f'Subject: {subject}\n\n{body}'
                    smtp.sendmail('chopeyourspot@gmail.com',email,msg)
                    logging.debug("OTP sent successfully!")
            except Exception as e:
                print(f'Failed to send OTP: {e}')

            request.session['correct_OTP'] = correct_OTP
            request.session['OTP_generated'] = True

    return render(request, '2faUserregistration.html', {
        'form': form
    })        

def Payment_view(request): #Send a mail acknowledging
    Current_login_data = request.session.get('login_data')
    company_data = request.session.get('company_data')

    if not Current_login_data:
        return redirect('.')
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            if len(str(form.cleaned_data['PaymentReference'])) != 0:
                
                ### DO THE SAVING TO DB HERE###

                first_name = Current_login_data['first_name']
                last_name = Current_login_data['last_name']
                username = Current_login_data['username']
                domain = Current_login_data['domain']
                password = Current_login_data['password']
                email = Current_login_data['email']
                user_Type = Current_login_data['user_Type']

                logindet = users(first_name = first_name, last_name = last_name, username = username, domain = domain, password = password, email = email, user_Type = user_Type)
                logindet.save()

                company_name = company_data['company_name']
                company_Address = company_data['company_Address']
                admin_officer = company_data['admin_officer']
                domain = company_data['domain']
                approved = company_data['approved']

                companydet = registeredDomains(company_name = company_name, company_Address=company_Address, admin_officer = admin_officer, domain = domain, approved = approved)
                companydet.save()

                paymentdet = payments(domain = domain, PaymentReference = str(form.cleaned_data['PaymentReference']))
                paymentdet.save()
                if not request.session.get('emailSent'):
                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        email = Current_login_data['email']
                        msg='Dear '+str(first_name)+',\nWe have registered your request to register your company.\nOur System Administrators would acknowledge your request and send a confirmation email within 3 working days. '+'\n\nWarm Regards\nChopeYourSpot Team '
                        sub='Company Registration Acknowledgement'

                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('chopeyourspot@gmail.com','ybacagvwwwacqukr')    
                        subject = sub
                        body = msg
                        msg = f'Subject: {subject}\n\n{body}'
                        smtp.sendmail('chopeyourspot@gmail.com',email,msg)
                        request.session['emailSent'] = True
                
                #MOVE ALL THESE TO NEXT PAGE - also include the specific redirect to login page if these are not present
                del request.session['emailSent'] #MOVE THIS TO NEXT PAGE - compulsory
                del request.session['login_data']
                del request.session['company_data']

                #########################
                return redirect('adminsuccess') 
                
            else:
                form.add_error('PaymentReference', 'Enter Transaction Reference')
                
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {
        'form': form
    })      


