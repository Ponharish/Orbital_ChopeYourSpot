from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from login.models import registeredDomains, users
from Company_Admin.models import ListOfCommonSpaces, ListOfBookings, ListOfPastBookings
from django.views.decorators.cache import never_cache
from System_Admin.models import Message
from .makeabookingform import makeabookingform
from .cancelBookingForm import cancelbookingform
from .startsessionform import startsessionform
from .endsessionform import endsessionform
from .chatempepeForm import chatempepeForm
from datetime import datetime, date, timedelta

# Create your views here.


@never_cache
def Employer_Employee_Dashboard(request): #OK
    first_name = request.session['Current_login_data']['first_name']
    company = registeredDomains.objects.get(domain = request.session['Current_login_data']['domain'])
    return render(request, 'Employer_Employee_Dashboard.html', {'first_name': first_name, 'company' : company.company_name})

@never_cache
def logoutpageusr(request):
    request.session.pop('Current_login_data', None)
    return render(request, 'logoutpageusr.html')

@never_cache
def viewbookings(request):
    username = request.session['Current_login_data']['username']
    domain = request.session['Current_login_data']['domain']
    bookings = ListOfBookings.objects.filter(domain = domain, username = username)
    is_empty = not bookings.exists() # Check if queryset is empty
    return render(request, 'ViewBookingsemp.html', {'bookings': bookings, 'is_empty': is_empty})

@never_cache
def viewlistofcommonspaces(request):
    spacelist = ListOfCommonSpaces.objects.filter(domain = request.session['Current_login_data']['domain'])
    is_empty = not spacelist.exists() # Check if queryset is empty
    return render(request, 'viewlistofcommonspacesuser.html', {'spaces': spacelist, 'is_empty': is_empty})

@never_cache
def makeabookinguser(request):
    if request.method == 'POST':
        form = makeabookingform(request.POST)
        if form.is_valid():
            placeid = form.cleaned_data.get('placeid')
            username = request.session['Current_login_data']['username']
            booking_date = form.cleaned_data.get('booking_date')
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            domain = request.session['Current_login_data']['domain']

            #Check user
            userfor = users.objects.filter(username = username, domain = domain) 
            is_empty = not userfor.exists() 
            
            if is_empty:
                form.add_error('username', 'Invalid Username') 
                return render(request, 'makeabookinguser.html', {'form': form})

            #check if past date is inputted
            if booking_date < datetime.today().date():
                form.add_error('booking_date', 'Booking date cannot be in the past') 
                return render(request, 'makeabookinguser.html', {'form': form})
            

            # formatted_date = booking_date.strftime('%m/%d/%Y')
            day_of_week = booking_date.strftime('%A') 
            today = date.today()
            
            #Check if such a place exists
            placeavailability = ListOfCommonSpaces.objects.filter(id = placeid, domain = domain)
            is_empty = not placeavailability.exists() 
            
            if is_empty:
                form.add_error('placeid', 'Invalid Location') 
                return render(request, 'makeabookinguser.html', {'form': form})

            #Make sure booking can only be done 50 days in advance
            max_booking_date = today + timedelta(days=50)

            if booking_date > max_booking_date:
                form.add_error('booking_date', "Bookings can only be made up to 50 days in advance")
                return render(request, 'makeabookinguser.html', {'form': form})

            #Handle case where start time is given to be after end time
            if start_time >= end_time:
                form.add_error('start_time', 'Invalid timing entered. End time is before Start time.')
                return render(request, 'makeabookinguser.html', {'form': form})
            
            #if booking for today, make sure no past booking is made
            if booking_date == datetime.today().date():
                current_time = datetime.now().time()
                if start_time < current_time:# or end_time < current_time:
                    form.add_error('start_time', 'Invalid timing entered. Start time is before current time')
                    return render(request, 'makeabookinguser.html', {'form': form})

            
            
            place = placeavailability.first()
            placeavail = place.availability

            #Check if the place is available on given day
            if not (placeavail.get(day_of_week.lower())).get('available'):
                form.add_error('booking_date', 'Place is not available in the specified date') 
                return render(request, 'makeabookinguser.html', {'form': form})


            start_time_ck = datetime.strptime((placeavail.get(day_of_week.lower())).get('start_time'), '%I:%M %p').time()
            end_time_ck = datetime.strptime((placeavail.get(day_of_week.lower())).get('end_time'), '%I:%M %p').time()
            if start_time_ck > start_time:
                form.add_error('start_time', 'Place is not available in the specified start time') 
                return render(request, 'makeabookinguser.html', {'form': form})
            
            if end_time_ck < end_time:
                form.add_error('start_time', 'Place is not available in the specified end time') 
                return render(request, 'makeabookinguser.html', {'form': form})
  
            bookinghistory = ListOfBookings.objects.filter(placeid = placeid, domain = domain, bookingdate = booking_date)
 
            for booking in bookinghistory:
                existing_start_time = booking.starttime
                existing_end_time = booking.endtime
                

                if (existing_start_time <= start_time < existing_end_time) or (existing_start_time < end_time <= existing_end_time) or (start_time <= existing_start_time and end_time >= existing_end_time):
                    form.add_error('start_time', 'The booking overlaps with an existing booking.')
                    return render(request, 'makeabookinguser.html', {'form': form})
            
            currentbookingdetails = {
                'placeid' : placeid,
                'username' : username,
                'booking_date' : booking_date.strftime('%Y-%m-%d'),
                'bookingday' : day_of_week,
                'start_time': start_time.strftime('%H:%M:%S'),
                'end_time': end_time.strftime('%H:%M:%S'),
                'domain' : domain
            }

            request.session['current_booking_detail'] = currentbookingdetails
            return redirect('makeabookinguserconfirm')
            
    else:
        form = makeabookingform() 

    return render(request, 'makeabookinguser.html', {
        'form': form
    })    

@never_cache
def makeabookinguserconfirm(request):
    currentbookingdetails = request.session.get('current_booking_detail')
    return render(request, 'confirmbookgingmadeuser.html', {'booking_details': currentbookingdetails})

    
@never_cache
def makeabookingusersuccess(request):
    currentbookingdetails = request.session.get('current_booking_detail')

    if request.method =='GET':
        currentbookingdetails = request.session.get('current_booking_detail')
        start_time = datetime.strptime(currentbookingdetails['start_time'], '%H:%M:%S').time()
        end_time = datetime.strptime(currentbookingdetails['end_time'], '%H:%M:%S').time()
        booking_date = datetime.strptime(currentbookingdetails['booking_date'], '%Y-%m-%d').date()
        placeid = currentbookingdetails['placeid']
        username = currentbookingdetails['username']
        bookingday = currentbookingdetails['bookingday']
        domain = currentbookingdetails['domain']
        currentstatus = 'Scheduled'

        spacedet = ListOfBookings(
                                placeid = placeid, 
                                domain = domain, 
                                username = username, 
                                bookingdate = booking_date, 
                                bookingday = bookingday, 
                                starttime = start_time, 
                                endtime = end_time,
                                currentstatus = currentstatus
                                )
        spacedet.save()

        request.session.pop('current_booking_detail')
    return render(request, 'bookingsuccessuser.html')


@never_cache
def cancelBookinguser(request):
    if request.method == 'POST':
        form = cancelbookingform(request.POST)
        if form.is_valid():
            bookingid = form.cleaned_data.get('idfield')


            domain = request.session['Current_login_data']['domain']
            username = request.session['Current_login_data']['username']
            placelist = ListOfBookings.objects.filter(id = bookingid, domain = domain, username=username) 
            is_empty = not placelist.exists() 
            
            if is_empty:
                form.add_error('idfield', 'Invalid Booking ID') 
                return render(request, 'cancelBookingFormuser.html', {'form': form})
            
            placelist = ListOfBookings.objects.filter(id = bookingid, currentstatus = 'Scheduled', domain = domain)
            is_empty = not placelist.exists() 
            if is_empty:
                form.add_error('idfield', 'The booking cannot be cancelled at the moment. Please verify the status of the session') 
                return render(request, 'cancelBookingFormuser.html', {'form': form})
            

            #create a seassion cookie and remove it later!!
            request.session['current_booking_to_delete'] = bookingid
            return redirect('cancelBookingConfirmationuser')

            
    else:
        form = cancelbookingform() 

    return render(request, 'cancelBookingFormuser.html', {
        'form': form
    }) 


@never_cache
def cancelBookingConfirmationuser(request):
    bookingid = request.session.get('current_booking_to_delete')
    spacelist = ListOfBookings.objects.filter(id = bookingid).last()
    place_details = {
        'id':bookingid,
        'placeid':spacelist.placeid,
        'username':spacelist.username,

        'bookingdate':spacelist.bookingdate,
        'bookingday':spacelist.bookingday,
        'starttime':spacelist.starttime,
        'endtime':spacelist.endtime,
    }
    return render(request, 'cancelbookingconfirmationuser.html', {'place_details': place_details})

@never_cache
def cancelBookingSuccessuser(request):
    if request.method =='GET':
        bookingid = request.session.get('current_booking_to_delete')
        domain = request.session['Current_login_data']['domain']
        placelistbk = ListOfBookings.objects.filter(id = bookingid).last()

        spacedet = ListOfPastBookings(
                                    bookingid = bookingid,
                                    placeid = placelistbk.placeid, 
                                    domain = placelistbk.domain, 
                                    username = placelistbk.username,
                                    bookingdate = placelistbk.bookingdate,
                                    bookingday = placelistbk.bookingday,
                                    starttime = placelistbk.starttime,
                                    endtime = placelistbk.endtime,
                                    currentstatus = 'Cancelled'
                                    )
        spacedet.save()

        placelistbk.delete()





        request.session.pop('current_booking_to_delete')
    return render(request, 'cancelbookingsuccessmessageuser.html')

@never_cache
def startsession(request):
    if request.method == 'POST':
        form = startsessionform(request.POST)
        if form.is_valid():
            bookingid = form.cleaned_data.get('idfield')


            domain = request.session['Current_login_data']['domain']
            username = request.session['Current_login_data']['username']
            placelist = ListOfBookings.objects.filter(id = bookingid, domain = domain, username=username) 
            is_empty = not placelist.exists() 
            
            if is_empty:
                form.add_error('idfield', 'Invalid Booking ID') 
                return render(request, 'startSession.html', {'form': form})
            
            placelist = ListOfBookings.objects.filter(id = bookingid, currentstatus = 'Scheduled', domain = domain)
            is_empty = not placelist.exists() 
            if is_empty:
                form.add_error('idfield', 'The booking you have selected is currently ongoing or has been cancelled') 
                return render(request, 'startSession.html', {'form': form})
            placelist = ListOfBookings.objects.filter(id = bookingid, currentstatus = 'Scheduled', domain = domain).last()
            start_datetime = datetime.combine(datetime.today(), placelist.starttime)
            end_datetime = datetime.combine(datetime.today(), placelist.endtime)
            if not (start_datetime <= datetime.now() <= end_datetime):
                    form.add_error('idfield', 'Please start session within the time frame for your booking')
                    return render(request, 'startSession.html', {'form': form})
            
            #create a seassion cookie and remove it later!!
            request.session['current_booking_to_start'] = bookingid
            return redirect('startSessionconfirmation')

            
    else:
        form = cancelbookingform() 

    return render(request, 'startSession.html', {
        'form': form
    }) 

@never_cache
def startSessionconfirmation(request):
    bookingid = request.session.get('current_booking_to_start')
    spacelist = ListOfBookings.objects.filter(id = bookingid).last()
    place_details = {
        'id':bookingid,
        'placeid':spacelist.placeid,
        'username':spacelist.username,

        'bookingdate':spacelist.bookingdate,
        'bookingday':spacelist.bookingday,
        'starttime':spacelist.starttime,
        'endtime':spacelist.endtime,
    }
    return render(request, 'startSessionConfirmation.html', {'place_details': place_details})


@never_cache
def startsessionsuccess(request):
    if request.method =='GET':
        bookingid = request.session.get('current_booking_to_start')
        domain = request.session['Current_login_data']['domain']
        placelistbk = ListOfBookings.objects.filter(id = bookingid).last()
        placelistbk.currentstatus = 'Ongoing'


        

        placelistbk.save()
        request.session.pop('current_booking_to_start')
    return render(request, 'startsessionsuccess.html')



@never_cache
def endsession(request):
    if request.method == 'POST':
        form = endsessionform(request.POST)
        if form.is_valid():
            bookingid = form.cleaned_data.get('idfield')


            domain = request.session['Current_login_data']['domain']
            username = request.session['Current_login_data']['username']
            placelist = ListOfBookings.objects.filter(id = bookingid, domain = domain, username=username) 
            is_empty = not placelist.exists() 
            
            if is_empty:
                form.add_error('idfield', 'Invalid Booking ID') 
                return render(request, 'endSession.html', {'form': form})
            
            placelist = ListOfBookings.objects.filter(id = bookingid, currentstatus = 'Ongoing', domain = domain)
            is_empty = not placelist.exists() 
            if is_empty:
                form.add_error('idfield', 'The session not currently active') 
                return render(request, 'endSession.html', {'form': form})
            

            #create a seassion cookie and remove it later!!
            request.session['current_booking_to_end'] = bookingid
            return redirect('endSessionconfirmation')

            
    else:
        form = cancelbookingform() 

    return render(request, 'endSession.html', {
        'form': form
    }) 

@never_cache
def endSessionconfirmation(request):
    bookingid = request.session.get('current_booking_to_end')
    spacelist = ListOfBookings.objects.filter(id = bookingid).last()
    start_datetime = datetime.combine(datetime.today(), spacelist.starttime)
    time_difference = datetime.now() - start_datetime
    duration = datetime(1, 1, 1) + time_difference
    formatted_duration = duration.strftime('%H hours and %M minutes')

    place_details = {
        'id':bookingid,
        'placeid':spacelist.placeid,
        'username':spacelist.username,

        'bookingdate':spacelist.bookingdate,
        'bookingday':spacelist.bookingday,
        'starttime':spacelist.starttime,
        'endtime':spacelist.endtime,
        'timelapsed': formatted_duration
    }
    return render(request, 'endSessionConfirmation.html', {'place_details': place_details})


@never_cache
def endsessionsuccess(request):
    if request.method =='GET':
        bookingid = request.session.get('current_booking_to_end')
        domain = request.session['Current_login_data']['domain']
        placelistbk = ListOfBookings.objects.filter(id = bookingid).last()
        
        spacedet = ListOfPastBookings(
                                    bookingid = bookingid,
                                    placeid = placelistbk.placeid, 
                                    domain = placelistbk.domain, 
                                    username = placelistbk.username,
                                    bookingdate = placelistbk.bookingdate,
                                    bookingday = placelistbk.bookingday,
                                    starttime = placelistbk.starttime,
                                    endtime = placelistbk.endtime,
                                    currentstatus = 'Completed'
                                    )
        spacedet.save()

        placelistbk.delete()
        request.session.pop('current_booking_to_end')
    return render(request, 'endsessionsuccess.html')



#CHAT FUNCTIONALITIES
@never_cache
def empepeinbox(request):
    
    messages = Message.objects.filter(receiver=request.session['Current_login_data']['username'], receiverdomain = request.session['Current_login_data']['domain'])
    is_empty = not messages.exists()
    return render(request, 'empepeinbox.html', {'messages': messages, 'is_empty': is_empty})

def empepesent(request):
    messages = Message.objects.filter(sender=request.session['Current_login_data']['username'], senderdomain = request.session['Current_login_data']['domain'])
    is_empty = not messages.exists()
    return render(request, 'empepesent.html', {'messages': messages, 'is_empty': is_empty})


def empepecompose(request):
    if request.method == 'POST':
        form = chatempepeForm(request.POST)
        if form.is_valid():
            sender = request.session['Current_login_data']['username']
            senderdomain = request.session['Current_login_data']['domain']
            receiver = form.cleaned_data.get('username').strip()  
            receiverdomain = form.cleaned_data.get('domain').strip()  
            subject = form.cleaned_data.get('subject').strip()    
            message = form.cleaned_data.get('message').strip()    

            mailsetails = Message(sender = sender, senderdomain = senderdomain, receiver = receiver, receiverdomain =receiverdomain, subject = subject, content = message)
            mailsetails.save()

            return redirect('empepesentack')



    else:
        form = chatempepeForm()

    return render(request, 'chatcomposeempepe.html', {
        'form': form,
    })   

def empepesentack(request):
    return render(request, 'mailcomposesuccessempepe.html')