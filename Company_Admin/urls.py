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
]