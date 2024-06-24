from django.urls import path
from . import views


urlpatterns = [
    path('', views.Company_Admin_Dashboard, name = 'Company_Admin_Dashboard'),
    path('logoutpageca', views.logoutpageca, name = 'logoutpageca'),
    path('viewregisteredemployees', views.viewregisteredemployees, name = 'viewregisteredemployees'),
    path('addcommonspace', views.addcommonspace, name = 'addcommonspace'),
    path('addcommonspacesuccess', views.addcommonspacesuccess, name = 'addcommonspacesuccess'),
    path('viewlistofcommonspaces', views.viewlistofcommonspaces, name = 'viewlistofcommonspaces'),
    path('removecommonspace', views.removecommonspace, name = 'removecommonspace'),
    path('removecompanyconfirmation', views.removecompanyconfirmation, name = 'removecompanyconfirmation'),
    path('removefacilitysuccess', views.removefacilitysuccess, name = 'removefacilitysuccess'),
    path('makeabookingadm', views.makeabookingadm, name = 'makeabookingadm'),
    path('makeabookingadmsuccess', views.makeabookingadmsuccess, name = 'makeabookingadmsuccess'),
    path('makeabookingadmconfirm', views.makeabookingadmconfirm, name = 'makeabookingadmconfirm'),
    path('viewbookings', views.viewbookings, name = 'viewbookings'),
    path('cancelBooking', views.cancelBooking, name = 'cancelBooking'),
    path('cancelBookingConfirmation', views.cancelBookingConfirmation, name = 'cancelBookingConfirmation'),
    path('cancelBookingSuccess', views.cancelBookingSuccess, name = 'cancelBookingSuccess'),
]