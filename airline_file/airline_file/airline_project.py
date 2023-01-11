from django.db import models
from django.forms import Form
from django.db import connections
# models.py
# Model Classes
class Customer_dataInsert(models.Model):
    F_name=models.CharField(max_length=15)
    customer_age=models.IntegerField(max_length=100)
    customer_gender=models.CharField(max_length=10)
    customer_address=models.CharField(max_length=100)
    mobile_no=models.IntegerField()
    email=models.CharField(max_length=30)
    Date_of_birth=models.DateField(auto_now=False,auto_now_add=False,blank=True)
    class Meta:
        db_table="login_customer_detail"
class Show_flights(models.Model):
    id=models.IntegerField(primary_key=True)
    src_cityname=models.CharField(max_length=15)
    src_state=models.CharField(max_length=15)
    dest_cityname=models.CharField(max_length=15)
    dest_state=models.CharField(max_length=15)
    class Meta:
        db_table="plane_src_dest" 
class Show_flightID(models.Model):
    id=models.IntegerField(primary_key=True)
    flight_code=models.CharField(max_length=15)
    flight_state=models.CharField(max_length=25)
    flight_cityname=models.CharField(max_length=30)
    class Meta:
        db_table="plane_details"
class Customer_flightBook(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    customer_age=models.IntegerField(max_length=100)
    mobile_no=models.IntegerField()
    email=models.CharField(max_length=30)
    src_cityname=models.CharField(max_length=15)
    src_state=models.CharField(max_length=15)
    dest_cityname=models.CharField(max_length=15)
    dest_state=models.CharField(max_length=15)
    booking_date=models.DateField(auto_now=False,auto_now_add=False,blank=True)
    class Meta:
        db_table="customer_flight_detail"
class Login_detail(models.Model):
    f_name=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    class Meta:
        db_table="customer_login_detail"
class Feedback(models.Model):
    c_name=models.CharField(max_length=25)
    c_email=models.CharField(max_length=35)
    contact=models.IntegerField(max_length=11)
    message=models.CharField(max_length=100)
    class Meta:
        db_table="feedback_detail"
