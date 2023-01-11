"""airline_file URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import airline_views
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',airline_views.Home_page),
    path('website_home.html/',airline_views.Login_user, name="website_home"),  #<-----
    path('airline_booking_customer_detail.html/',airline_views.InsertRecord,name='airline_booking_customer_detail'),
    path('website_home.html/',airline_views.Home_page,name='website_home'),
    path('airline_contact_us.html/',airline_views.Contact_us,name='airline_contact_us'),
    path('airline_website_payment_detail.html/',airline_views.Payment_detail,name='airline_website_payment_detail'),
    path('airline_booking_cancelation.html/',airline_views.Cancel_ticket,name='airline_booking_cancelation'),
    path('airline_booking_journey_detail.html/',airline_views.Journey_info,name='airline_booking_journey_detail'),
    path('air_plane_about_us.html/',airline_views.About_us,name='air_plane_about_us')
]
