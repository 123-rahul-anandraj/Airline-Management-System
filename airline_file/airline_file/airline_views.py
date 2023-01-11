from django.shortcuts import render,redirect
from .airline_project import Customer_dataInsert
from django.contrib import messages
from django.forms import ModelForm
from .airline_project import Show_flights,Show_flightID,Customer_flightBook,Login_detail,Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from datetime import date,datetime
from django.http import HttpResponse, HttpResponseRedirect
# views.py
def Login_user(request):
    login_user=Login_detail()
    if request.method=='POST':
        if request.POST.get('logout'):
            messages.info(request)
            return render(request,'website_home.html')
        else:
            username=request.POST.get('username')
            password=request.POST.get('password')
            check_if_user_exists = Login_detail.objects.filter(username=username,password=password)
            print(username, password, check_if_user_exists)
            if check_if_user_exists:
                messages.info(request,'Login successfully')
                return render(request,'website_home.html')
            else:
                print('user does not exists')
                return render(request,'website_home.html')
            
    else:
        return render(request,'website_home.html')

#@login_required(login_url='website_home.html')
def InsertRecord(request):
    if request.method=='POST':
        if request.POST.get('F_name') and request.POST.get('customer_age') and request.POST.get('customer_gender') and request.POST.get('customer_address') and request.POST.get('mobile_no') and request.POST.get('email') and request.POST.get('Date_of_birth'):
            saverecord=Customer_dataInsert()
            saverecord.F_name=request.POST.get('F_name')
            saverecord.customer_age=request.POST.get('customer_age')
            saverecord.customer_gender=request.POST.get('customer_gender')
            saverecord.customer_address=request.POST.get('customer_address')
            saverecord.mobile_no=request.POST.get('mobile_no')
            saverecord.email=request.POST.get('email')
            saverecord.Date_of_birth=request.POST.get('Date_of_birth')
            birthdate_object = datetime.strptime(saverecord.Date_of_birth, '%Y-%m-%d').date()
            if(date.today() < birthdate_object):
                datemsg='Please do not enter future dates as your Date-of-Birth!!'
                return render(request,'airline_booking_customer_detail.html',{"obj_datemsg":datemsg})
            else:
                print(saverecord.Date_of_birth)
                saverecord.save()
                if request.POST.get('F_name') and request.POST.get('username') and request.POST.get('password'):
                    save_login=Login_detail()
                    save_login.f_name=request.POST.get('F_name')
                    save_login.username=request.POST.get('username')
                    save_login.password=request.POST.get('password')
                    save_login.save()
                messages.info(request,'Record saves successfully...')
                return render(request,'airline_booking_customer_detail.html')
    else:
        return render(request,'airline_booking_customer_detail.html')
def Home_page(request):
    return render(request,'website_home.html')
def About_us(request):
    return render(request,'air_plane_about_us.html')
def Contact_us(request):
    if request.method=='POST':
        if request.POST.get('c_name') and request.POST.get('c_email') and request.POST.get('contact') and request.POST.get('message'):
            feedback_save=Feedback()
            feedback_save.c_name=request.POST.get('c_name')
            feedback_save.c_email=request.POST.get('c_email')
            feedback_save.contact=request.POST.get('contact')
            feedback_save.message=request.POST.get('message')
            feedback_save.save()
    return render(request,'airline_contact_us.html')
def Payment_detail(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('customer_age') and request.POST.get('mobile_no') and request.POST.get('email') and request.POST.get('src_cityname') and request.POST.get('src_state') and request.POST.get('dest_cityname') and request.POST.get('dest_state'):
            bookflight=Customer_flightBook()
            bookflight.name=request.POST.get('name')
            bookflight.customer_age=request.POST.get('customer_age')
            bookflight.mobile_no=request.POST.get('mobile_no')
            bookflight.email=request.POST.get('email')
            bookflight.src_cityname=request.POST.get('src_cityname')
            bookflight.src_state=request.POST.get('src_state')
            bookflight.dest_cityname=request.POST.get('dest_cityname')
            bookflight.dest_state=request.POST.get('dest_state')
            bookflight.booking_date=request.POST.get('booking_date')
            bookingdate_object = datetime.strptime(bookflight.booking_date, '%Y-%m-%d').date()
            if(date.today() > bookingdate_object):
                datemsg='Please do not enter past dates!!'
                return render(request,'airline_website_payment_detail.html',{"obj_datemsg":datemsg})
            else:
                bookflight.save()
                messages.success(request,'Flight booked successfully...')
                return render(request,'airline_website_payment_detail.html')
    return render(request,'airline_website_payment_detail.html')
def Cancel_ticket(request):
    if request.method=="GET":
        return render(request,'airline_booking_cancelation.html')
    if request.method=='POST':
        if request.POST.get('Cancellation_date') and request.POST.get('name'):
            cancel_ticket_date=Customer_flightBook()
            cancel_ticket_id=Show_flightID()
            try:
                del_flight=Customer_flightBook.objects.all().filter(booking_date=request.POST.get("Cancellation_date")) #.filter(name=request.POST.get("name"))
                print(del_flight)
                del_flight.delete()
                messages.success(request,'Flight cancelled successfully...')
            except:
                messages.success(request,'No booked flights of this date is found !')
        return render(request,'airline_booking_cancelation.html')
def Journey_info(request):
    flight_obj=Show_flights()                 
    flight_id=Show_flightID()
    if request.method=="GET":
        return render(request,'airline_booking_journey_detail.html')
    if request.method=='POST':
        if request.POST.get("from_country") and request.POST.get("to_country"):
            src=Show_flights.objects.filter(src_state=request.POST.get("from_country"), dest_state=request.POST.get("to_country"))
            fid=Show_flightID.objects.filter(flight_state=request.POST.get("from_country"))
            return render(request,'airline_booking_journey_detail.html', {"object": src , "obj_id":fid } )
        return render(request,'airline_booking_journey_detail.html')
