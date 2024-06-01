from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name = 'loginPage'),
    path('2falogin', views._2faLogin_view, name = '2falogin'),
    path('createAccount', views.createAccount, name = 'createAccount'), 
    path('resetPassword', views.resetPassword, name = 'resetPassword'), 


    path('registerUser', views.userRegister_view, name = 'registerUser'), 
    path('handle_redirect_register', views.handle_redirect_register, name='handle_redirect_register'),

    path('2faregister', views._2faRegister_view, name = '2faregister'), 
    path('usersuccess', views.usersuccess, name = 'usersuccess'), 
    path('registerAdmin', views.AdminRegister_view, name = 'registerAdmin'), 
    path('payment', views.Payment_view, name = 'payment'), 
    path('adminsuccess', views.adminsuccess, name = 'adminsuccess'), 
    
]

#CREATE THE DB
#Add the functionality for the other forms as well
#create 3 apps - user, company admin, system admin
