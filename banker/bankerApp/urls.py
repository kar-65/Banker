from . import  views
from django.urls import path
app_name='bankerApp'
urlpatterns = [
    path('',views.bankIndex,name='bankIndex'),
    path('Register', views.Register, name='Register'),
    path('login', views.Login, name='Login'),
    path('home', views.Home, name='Home'),
    path('requirments', views.requirments ,name='requirments'),
    path('logout', views.logout, name='logout'),
    path('successmsg',views.successmsg, name='successmsg')
]