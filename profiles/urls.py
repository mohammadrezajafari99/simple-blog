
from django.urls import path
from .views import profile,account,updateprofile,deleteprofile,register_user,login_user,logout_user


urlpatterns = [
    path('profile/<str:pk>', profile,name='profile'),
    path('account',account,name='account'),
    path('updateprofile',updateprofile,name='updateprofile'),
    path('deleteprofile',deleteprofile,name='deleteprofile'),
    path('register',register_user,name='register'),
    path('login',login_user,name='login'),
    path('logout',logout_user,name='logout')
   
]
