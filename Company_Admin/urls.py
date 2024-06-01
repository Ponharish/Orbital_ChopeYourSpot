from django.urls import path
from . import views


urlpatterns = [
    path('', views.Company_Admin_Dashboard, name = 'Company_Admin_Dashboard'),
]