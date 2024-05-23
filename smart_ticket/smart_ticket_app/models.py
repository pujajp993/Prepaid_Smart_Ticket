from django.db import models
from django. contrib. auth.models import AbstractUser
import random

class User(AbstractUser):  
    
    Address=models.CharField(max_length=100,verbose_name="Address")
    Phone_no=models.IntegerField(verbose_name="Phone")
    DOB=models.DateField(verbose_name="Date of Joining")
    Cd_type=models.CharField(max_length=20,verbose_name="Card Type")
    District=models.CharField(max_length=25,verbose_name="District")
    State=models.CharField(max_length=25,verbose_name="State")
    Aadhar_no=models.CharField(max_length=15,verbose_name="AAdhar Number")
    Role=models.CharField(max_length=10,verbose_name="Role")
    class Meta:  
        db_table = "tb_user" 

class Staff(User):
    # Add staff-specific fields or methods here
    Status=models.IntegerField(verbose_name="Status")
    Staff_id=models.IntegerField(verbose_name="Staff Id")
    # random_string = generate_random_string(20) 
    class Meta:
        db_table = "tbl_staff"



class tbl_bustype(models.Model):
   Bus_type=models.CharField(max_length=25)

class tbl_schedule(models.Model):
   schedule_name=models.CharField(max_length=25)

class tbl_bus(models.Model):
    bus_no=models.CharField(max_length=25,verbose_name="Bus No")
    bus_type_id=models.ForeignKey(tbl_bustype,on_delete=models.CASCADE)
    Source=models.CharField(max_length=25,verbose_name="Bus Starting Point")
    Destination=models.CharField(max_length=25,verbose_name="Bus Ending Point")
    Start_time=models.TimeField()
    End_time=models.TimeField()
    schedule_id=models.ForeignKey(tbl_schedule,on_delete=models.CASCADE,null=True)
    bus_image=models.FileField(upload_to='media')
    
    
class tbl_fare(models.Model):
    bus_type_id=models.ForeignKey(tbl_bustype,on_delete=models.CASCADE)
    min_charge=models.IntegerField()


class tbl_bank_name(models.Model):
    b_name=models.CharField(max_length=25,verbose_name="Bank Name")

class tbl_bank_account(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    holder_name=models.CharField(max_length=30,verbose_name="Card Holder name in card")
    bank_name=models.CharField(max_length=25,verbose_name="Bank Name")
    account_number=models.CharField(max_length=25,verbose_name="Bank Account No")
    cvv=models.IntegerField(verbose_name="CVV")
    month=models.CharField(max_length=10,verbose_name="Card Expiry mont")
    year=models.IntegerField(verbose_name="yaer of Expiry")
    amount=models.IntegerField(verbose_name="Cash in bank")

class tbl_card(models.Model):
    card_type=models.CharField(max_length=25,verbose_name="Card Type")
    card_prize=models.IntegerField()

class tbl_smartcard(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    card_prize=models.IntegerField(verbose_name="Card Prize")
    valid_from=models.DateField(verbose_name="Card Valid from")
    valid_to=models.DateField(verbose_name="Card Valid To")
    district=models.CharField(max_length=25,verbose_name="Card_valid_district")
    payment_status=models.IntegerField(verbose_name="Card Fee Payment")

class tbl_alert(models.Model):
    email=models.EmailField(max_length=25,verbose_name="Email")
    name=models.CharField(max_length=25,verbose_name="Name")
    message=models.CharField(max_length=25,verbose_name="Message")

class tbl_complaint(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject=models.EmailField(max_length=25,verbose_name="Subject")
    description=models.CharField(max_length=25,verbose_name="Description")
    complaint_replay=models.CharField(max_length=25,verbose_name="Complaint_replay")
    status=models.CharField(max_length=15,verbose_name="Status")
