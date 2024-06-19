from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime, date, timedelta
from login.models import registeredDomains
from login.models import users 
from .models import ListOfCommonSpaces, ListOfBookings
from django.views.decorators.cache import never_cache
from .addcommonspaceform import addcommonspaceform
from .removecommonspaceform import removecompanyform
from .makeabookingform import makeabookingform

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

@never_cache
def viewregisteredemployees(request):
    userslist = users.objects.filter(domain = request.session['Current_login_data']['domain'])
    is_empty = not userslist.exists() # Check if queryset is empty
    return render(request, 'viewregisteredemployees.html', {'users': userslist, 'is_empty': is_empty})

@never_cache
def addcommonspacesuccess(request):
    return render(request, 'placeregisteredsuccessmessage.html')


@never_cache
def addcommonspace(request):
    if request.method == 'POST':
        form = addcommonspaceform(request.POST)
        if form.is_valid():

            space_name = form.cleaned_data.get('space_name')

            domain = request.session['Current_login_data']['domain']
            placelist = ListOfCommonSpaces.objects.filter(domain = domain, SpaceName = space_name)
            is_empty = not placelist.exists() 
            if not is_empty:
                form.add_error('space_name', 'This place exists')
                return render(request, 'addcommonspace.html', {'form': form})




            available_monday = form.cleaned_data.get('available_monday')
            monday_start_time = form.cleaned_data.get('monday_start_time')
            monday_end_time = form.cleaned_data.get('monday_end_time')

            available_tuesday = form.cleaned_data.get('available_tuesday')
            tuesday_start_time = form.cleaned_data.get('tuesday_start_time')
            tuesday_end_time = form.cleaned_data.get('tuesday_end_time')

            available_wednesday = form.cleaned_data.get('available_wednesday')
            wednesday_start_time = form.cleaned_data.get('wednesday_start_time')
            wednesday_end_time = form.cleaned_data.get('wednesday_end_time')

            available_thursday = form.cleaned_data.get('available_thursday')
            thursday_start_time = form.cleaned_data.get('thursday_start_time')
            thursday_end_time = form.cleaned_data.get('thursday_end_time')

            available_friday = form.cleaned_data.get('available_friday')
            friday_start_time = form.cleaned_data.get('friday_start_time')
            friday_end_time = form.cleaned_data.get('friday_end_time')

            available_saturday = form.cleaned_data.get('available_saturday')
            saturday_start_time = form.cleaned_data.get('saturday_start_time')
            saturday_end_time = form.cleaned_data.get('saturday_end_time')

            available_sunday = form.cleaned_data.get('available_sunday')
            sunday_start_time = form.cleaned_data.get('sunday_start_time')
            sunday_end_time = form.cleaned_data.get('sunday_end_time')

            if not available_monday and not available_tuesday and not available_wednesday and not available_thursday and not available_friday and not available_saturday and not available_sunday:
                form.add_error('available_monday', 'None of day is selected. Please select atleast one day')
                return render(request, 'addcommonspace.html', {'form': form})


            if available_monday:
                if monday_start_time and monday_end_time:
                    if monday_start_time >= monday_end_time:
                        form.add_error('available_monday', 'Invalid timing entered for Monday. End time is before Start time.')
                        return render(request, 'addcommonspace.html', {'form': form})
                else:
                    form.add_error('available_monday', 'Monday start time or end time is missing')
                    return render(request, 'addcommonspace.html', {'form': form})
                

            if available_tuesday:
                if not (tuesday_start_time and tuesday_end_time):
                    form.add_error('available_tuesday', 'Tuesday start time or end time is missing')
                    return render(request, 'addcommonspace.html', {'form': form})
                if tuesday_start_time >= tuesday_end_time:
                    form.add_error('available_tuesday', 'Invalid timing entered for Tuesday. End time is before Start time.')
                    return render(request, 'addcommonspace.html', {'form': form})



            if available_wednesday:
                if not (wednesday_start_time and wednesday_end_time):
                    form.add_error('available_wednesday', 'Wednesday start time or end time is missing')
                    return render(request, 'addcommonspace.html', {'form': form})
                if wednesday_start_time >= wednesday_end_time:
                    form.add_error('available_wednesday', 'Invalid timing entered for Wednesday. End time is before Start time.')
                    return render(request, 'addcommonspace.html', {'form': form})


            if available_thursday:
                if not (thursday_start_time and thursday_end_time):
                    form.add_error('available_thursday', 'Thursday start time or end time is missing')
                    return render(request, 'addcommonspace.html', {'form': form})
                if thursday_start_time >= thursday_end_time:
                    form.add_error('available_thursday', 'Invalid timing entered for Thursday. End time is before Start time.')
                    return render(request, 'addcommonspace.html', {'form': form})


            if available_friday:
                if not (friday_start_time and friday_end_time):
                    form.add_error('available_friday', 'Friday start time or end time is missing')
                    return render(request, 'addcommonspace.html', {'form': form})
                if friday_start_time >= friday_end_time:
                    form.add_error('available_friday', 'Invalid timing entered for Friday. End time is before Start time.')
                    return render(request, 'addcommonspace.html', {'form': form})


            if available_saturday:
                if not (saturday_start_time and saturday_end_time):
                    form.add_error('available_saturday', 'Saturday start time or end time is missing')
                    return render(request, 'addcommonspace.html', {'form': form})
                if saturday_start_time >= saturday_end_time:
                    form.add_error('available_saturday', 'Invalid timing entered for Saturday. End time is before Start time.')
                    return render(request, 'addcommonspace.html', {'form': form})


            if available_sunday:
                if not (sunday_start_time and sunday_end_time):
                    form.add_error('available_sunday', 'Sunday start time or end time is missing')
                    return render(request, 'addcommonspace.html', {'form': form})
                if sunday_start_time >= sunday_end_time:
                    form.add_error('available_sunday', 'Invalid timing entered for Sunday. End time is before Start time.')
                    return render(request, 'addcommonspace.html', {'form': form})
            
            availability = {
                'monday': {
                    'available': available_monday,
                    'start_time': monday_start_time.strftime('%I:%M %p') if monday_start_time else None,
                    'end_time': monday_end_time.strftime('%I:%M %p') if monday_end_time else None
                },
                'tuesday': {
                    'available': available_tuesday,
                    'start_time': tuesday_start_time.strftime('%I:%M %p') if tuesday_start_time else None,
                    'end_time': tuesday_end_time.strftime('%I:%M %p') if tuesday_end_time else None
                },
                'wednesday': {
                    'available': available_wednesday,
                    'start_time': wednesday_start_time.strftime('%I:%M %p') if wednesday_start_time else None,
                    'end_time': wednesday_end_time.strftime('%I:%M %p') if wednesday_end_time else None
                },
                'thursday': {
                    'available': available_thursday,
                    'start_time': thursday_start_time.strftime('%I:%M %p') if thursday_start_time else None,
                    'end_time': thursday_end_time.strftime('%I:%M %p') if thursday_end_time else None
                },
                'friday': {
                    'available': available_friday,
                    'start_time': friday_start_time.strftime('%I:%M %p') if friday_start_time else None,
                    'end_time': friday_end_time.strftime('%I:%M %p') if friday_end_time else None
                },
                'saturday': {
                    'available': available_saturday,
                    'start_time': saturday_start_time.strftime('%I:%M %p') if saturday_start_time else None,
                    'end_time': saturday_end_time.strftime('%I:%M %p') if saturday_end_time else None
                },
                'sunday': {
                    'available': available_sunday,
                    'start_time': sunday_start_time.strftime('%I:%M %p') if sunday_start_time else None,
                    'end_time': sunday_end_time.strftime('%I:%M %p') if sunday_end_time else None
                }
            }

            description = form.cleaned_data.get('description')
            location = form.cleaned_data.get('location')
            Capacity = form.cleaned_data.get('capacity')
            ReservationRestrictions = form.cleaned_data.get('ReservationRestrictions')
            AdditionalFeatures = form.cleaned_data.get('AdditionalFeatures')

            spacedet = ListOfCommonSpaces(
                                        domain = domain, 
                                        SpaceName = space_name, 
                                        description = description, 
                                        location = location, 
                                        Capacity = Capacity, 
                                        availability = availability, 
                                        ReservationRestrictions = ReservationRestrictions,
                                        AdditionalFeatures = AdditionalFeatures
                                        )
            spacedet.save()

            return redirect('addcommonspacesuccess')

    else:
        form = addcommonspaceform()

    return render(request, 'addcommonspace.html', {
        'form': form,
    })   

@never_cache
def viewlistofcommonspaces(request):
    spacelist = ListOfCommonSpaces.objects.filter(domain = request.session['Current_login_data']['domain'])
    is_empty = not spacelist.exists() # Check if queryset is empty
    return render(request, 'viewlistofcommonspaces.html', {'spaces': spacelist, 'is_empty': is_empty})

@never_cache
def removecommonspace(request): 
    if request.method == 'POST':
        form = removecompanyform(request.POST)
        if form.is_valid():
            placeid = form.cleaned_data.get('idfield')
            ########################
            # TEST THE BELOW LATER #
            ########################

            domain = request.session['Current_login_data']['domain']
            placelist = ListOfCommonSpaces.objects.filter(id = placeid, domain = domain) 
            is_empty = not placelist.exists() 
            
            if is_empty:
                form.add_error('idfield', 'Invalid Location') 
                return render(request, 'removecompanyform.html', {'form': form})

            
            placelist = ListOfBookings.objects.filter(placeid = placeid, currentstatus = 'Ongoing', domain = domain)
            is_empty = not placelist.exists() 
            if not is_empty:
                form.add_error('idfield', 'There is an ongoing booking at this location. Ends this booking before removing the location') 
                return render(request, 'removecompanyform.html', {'form': form})

            #create a seassion cookie and remove it later!!
            request.session['current_location_to_delete'] = placeid
            return redirect('removecompanyconfirmation')

            
    else:
        form = removecompanyform() 

    return render(request, 'removecompanyform.html', {
        'form': form
    })    

@never_cache
def removecompanyconfirmation(request):
    placeid = request.session.get('current_location_to_delete')
    # request.session.pop('current_location_to_delete')
    spacelist = ListOfCommonSpaces.objects.filter(id = placeid).last()
    place_details = {
        'id':placeid,
        'domain':spacelist.domain,
        'SpaceName':spacelist.SpaceName,
        'description':spacelist.description,
        'location':spacelist.location,
        'Capacity':spacelist.Capacity,
        'availability':spacelist.availability,
        'ReservationRestrictions':spacelist.ReservationRestrictions,
        'AdditionalFeatures':spacelist.AdditionalFeatures
    }
    return render(request, 'removecompanyconfirmation.html', {'place_details': place_details})


@never_cache
def removefacilitysuccess(request):
    placeid = request.session.get('current_location_to_delete')
    domain = request.session['Current_login_data']['domain']

    placelist = ListOfCommonSpaces.objects.filter(id = placeid, domain = domain) 
    placelist.delete()

    placelistbk = ListOfBookings.objects.filter(placeid = placeid, domain = domain)
    placelistbk.delete()



    request.session.pop('current_location_to_delete')
    return render(request, 'placeremovalsuccessmessage.html')

@never_cache
def makeabookingadm(request):
    if request.method == 'POST':
        form = makeabookingform(request.POST)
        if form.is_valid():
            placeid = form.cleaned_data.get('placeid')
            username = form.cleaned_data.get('username')
            booking_date = form.cleaned_data.get('booking_date')
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            domain = request.session['Current_login_data']['domain']

            print('*DATA*')
            print(placeid)
            print(username)
            print(booking_date)
            print(start_time)
            print(end_time)
            print(domain)


            #Check user
            userfor = users.objects.filter(username = username, domain = domain) 
            is_empty = not userfor.exists() 
            
            if is_empty:
                form.add_error('username', 'Invalid Username') 
                return render(request, 'makeabooking.html', {'form': form})

            #check if past date is inputted
            if booking_date < datetime.today().date():
                form.add_error('booking_date', 'Booking date cannot be in the past') 
                return render(request, 'makeabooking.html', {'form': form})
            

            ##################################
            # MILESTONE 3 - CONFIGURE TIME   #
            # make sure that the time is in  #
            # sync with the company timezone #
            # if booking time is in the past #
            # raise error                    #
            ##################################
            #Default timezone provided is singapore

            # formatted_date = booking_date.strftime('%m/%d/%Y')
            day_of_week = booking_date.strftime('%A') 
            today = date.today()
            
            #Check if such a place exists
            placeavailability = ListOfCommonSpaces.objects.filter(id = placeid, domain = domain)
            is_empty = not placeavailability.exists() 
            
            if is_empty:
                form.add_error('placeid', 'Invalid Location') 
                return render(request, 'makeabooking.html', {'form': form})

            #Make sure booking can only be done 50 days in advance
            max_booking_date = today + timedelta(days=50)

            if booking_date > max_booking_date:
                form.add_error('booking_date', "Bookings can only be made up to 50 days in advance")
                return render(request, 'makeabooking.html', {'form': form})

            #Handle case where start time is given to be after end time
            if start_time >= end_time:
                form.add_error('start_time', 'Invalid timing entered. End time is before Start time.')
                return render(request, 'makeabooking.html', {'form': form})
            
            #if booking for today, make sure no past booking is made
            if booking_date == datetime.today().date():
                current_time = datetime.now().time()
                if start_time < current_time or end_time < current_time:
                    form.add_error('start_time', 'Invalid timing entered. Start or End time is before current time')
                    return render(request, 'makeabooking.html', {'form': form})

            
            
            place = placeavailability.first()
            placeavail = place.availability

            #Check if the place is available on given day
            if not (placeavail.get(day_of_week.lower())).get('available'):
                form.add_error('booking_date', 'Place is not available in the specified date') 
                return render(request, 'makeabooking.html', {'form': form})


            start_time_ck = datetime.strptime((placeavail.get(day_of_week.lower())).get('start_time'), '%I:%M %p').time()
            end_time_ck = datetime.strptime((placeavail.get(day_of_week.lower())).get('end_time'), '%I:%M %p').time()
            if start_time_ck > start_time:
                form.add_error('start_time', 'Place is not available in the specified start time') 
                return render(request, 'makeabooking.html', {'form': form})
            
            if end_time_ck < end_time:
                form.add_error('start_time', 'Place is not available in the specified end time') 
                return render(request, 'makeabooking.html', {'form': form})
            

            bookinghistory = ListOfBookings.objects.filter(id = placeid, domain = domain, bookingdate = booking_date)

            for booking in bookinghistory:
                existing_start_time = booking.starttime
                existing_end_time = booking.endtime

                if (existing_start_time <= start_time < existing_end_time) or (existing_start_time < end_time <= existing_end_time) or (start_time <= existing_start_time and end_time >= existing_end_time):
                    form.add_error('start_time', 'The booking overlaps with an existing booking.')
                    return render(request, 'makeabooking.html', {'form': form})
            
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
            return redirect('makeabookingadmconfirm')
            
    else:
        form = makeabookingform() 

    return render(request, 'makeabooking.html', {
        'form': form
    })    

@never_cache
def makeabookingadmconfirm(request):
    currentbookingdetails = request.session.get('current_booking_detail')
    return render(request, 'confirmbookgingmade.html', {'booking_details': currentbookingdetails})


    
@never_cache
def makeabookingadmsuccess(request):
    currentbookingdetails = request.session.get('current_booking_detail')
    #SAVE TO DB
    # placeid = request.session.get('current_location_to_delete')
    # domain = request.session['Current_login_data']['domain']

    # placelist = ListOfCommonSpaces.objects.filter(id = placeid, domain = domain) 
    # placelist.delete()

    # placelistbk = ListOfBookings.objects.filter(placeid = placeid, domain = domain)
    # placelistbk.delete()


    #DESERIALISING TIME FROM REQUEST.SESSION
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
    return render(request, 'bookingsuccessadm.html')



    