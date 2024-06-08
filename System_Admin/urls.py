from django.urls import path
from . import views


urlpatterns = [
    path('', views.System_Admin_Dashboard, name = 'System_Admin_Dashboard'),
    path('logoutpage', views.logoutpage, name = 'logoutpage'),
    path('viewlistofcompanies',views.viewlistofcompanies, name = 'viewlistofcompanies'),
    path('seependingrequest',views.seependingrequest, name = 'seependingrequest'),
]
