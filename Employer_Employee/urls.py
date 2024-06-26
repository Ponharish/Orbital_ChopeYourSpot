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
]