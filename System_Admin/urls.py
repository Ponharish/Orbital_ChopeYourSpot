from django.urls import path
from . import views


urlpatterns = [
    path('', views.System_Admin_Dashboard, name = 'System_Admin_Dashboard'),
]