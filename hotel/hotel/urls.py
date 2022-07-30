"""
hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""

from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('login/', views.login),
    path('list/', views.list),
    path('roombook/', views.roombook),
    path('loginpage/', views.loginpage),
    path('page/', views.page),
    
    path('first/',views.first),
    path('book/', views.book),
    
    path('update_booking/', views.update_booking),
    path('edit_booking/', views.edit_booking),
    path('all_booking/', views.all_booking),
    
    
    
    
    path('insert/', views.insert),
    path('update/', views.update),
    path('all_table/', views.all_table),
    path('editcategory/', views.editcategories),
    path('board/', views.board),
    path('rooms/', views.rooms),
    path('roomupdate/', views.roomupdate),
    path('editroom/', views.editroom),
    path('all_tableroom/', views.all_tableroom),
    
    
    path('guestinsert/', views.guestinsert), 
    path('editguest/', views.editguest),
    path('guestupdate/', views.guestupdate),  
    path('all_guest/', views.all_guest),
    
    path('check/', views.check),
    path('all_Check/',views.all_Check),   
    path('docheckout/',views.docheckout),
    path('all_checkout/',views.all_checkout)    
     
]
