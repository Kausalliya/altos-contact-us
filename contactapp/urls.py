
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('main',views.main,name='main'),
     path('adminpage',views.adminpage,name='adminpage'),
     path('adminlogin',views.adminlogin,name='adminlogin'),
     path('admin',views.admin,name='admin'),
     path('signout',views.signout,name='signout'),
     path('insertcontact',views.insertcontact,name='insertcontact'),
     path('admincontact',views.admincontact,name='admincontact'),
     path('adminvideo',views.adminvideo,name='adminvideo'),
     path('insertvideo',views.insertvideo,name='insertvideo'),
     path('deletecontact/<int:pk>',views.deletecontact,name='deletecontact')
]
