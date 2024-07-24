from django.urls import path
from . import views


urlpatterns = [
    path('', views.Employer_Employee_Dashboard, name = 'Employer_Employee_Dashboard'),
    path('logoutpageusr', views.logoutpageusr, name = 'logoutpageusr'),
    path('viewbookings', views.viewbookings, name = 'viewbookings'),
    path('viewlistofcommonspaces', views.viewlistofcommonspaces, name = 'viewlistofcommonspaces'),
    path('makeabookinguser', views.makeabookinguser, name = 'makeabookinguser'),
    path('makeabookingusersuccess', views.makeabookingusersuccess, name = 'makeabookingusersuccess'),
    path('makeabookinguserconfirm', views.makeabookinguserconfirm, name = 'makeabookinguserconfirm'),
    path('cancelBookinguser', views.cancelBookinguser, name = 'cancelBookinguser'),
    path('cancelBookingConfirmationuser', views.cancelBookingConfirmationuser, name = 'cancelBookingConfirmationuser'),
    path('cancelBookingSuccessuser', views.cancelBookingSuccessuser, name = 'cancelBookingSuccessuser'),
    path('startsession', views.startsession, name = 'startsession'),
    path('startSessionconfirmation', views.startSessionconfirmation, name = 'startSessionconfirmation'),
    path('startsessionsuccess', views.startsessionsuccess, name = 'startsessionsuccess'),
    path('endsession', views.endsession, name = 'endsession'),
    path('endSessionconfirmation', views.endSessionconfirmation, name = 'endSessionconfirmation'),
    path('endsessionsuccess', views.endsessionsuccess, name = 'endsessionsuccess'),
    
    path('empepeinbox',views.empepeinbox, name = 'empepeinbox'),
    path('empepesent',views.empepesent, name = 'empepesent'),
    path('empepecompose',views.empepecompose, name = 'empepecompose'),
    path('empepesentack',views.empepesentack, name = 'empepesentack'),
]