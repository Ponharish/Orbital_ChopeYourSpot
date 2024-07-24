from django.urls import path
from . import views


urlpatterns = [
    path('', views.System_Admin_Dashboard, name = 'System_Admin_Dashboard'),
    path('logoutpage', views.logoutpage, name = 'logoutpage'),
    path('viewlistofcompanies',views.viewlistofcompanies, name = 'viewlistofcompanies'),
    path('seependingrequest',views.seependingrequest, name = 'seependingrequest'),
    path('approveorrejectcompanies',views.approveorrejectcompanies, name = 'approveorrejectcompanies'),
    path('approveorrejectcompanyinformation',views.approveorrejectcompanyinformation, name = 'approveorrejectcompanyinformation'),
    path('approvecompanymessage',views.approvecompanymessage, name = 'approvecompanymessage'),
    path('rejectcompanymessage',views.rejectcompanymessage, name = 'rejectcompanymessage'),
    path('approvecompanymessagetoask',views.approvecompanymessagetoask, name = 'approvecompanymessagetoask'),
    path('rejectcompanymessagetoask',views.rejectcompanymessagetoask, name = 'rejectcompanymessagetoask'),
    path('sysadminbox',views.sysadminbox, name = 'sysadminbox'),
    path('sysadmsent',views.sysadmsent, name = 'sysadmsent'),
    path('sysadmcompose',views.sysadmcompose, name = 'sysadmcompose'),
    path('sysadmsentack',views.sysadmsentack, name = 'sysadmsentack'),

]
