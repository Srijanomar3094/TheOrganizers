from django.db import models
from user.models import User_details
from django.contrib.auth.models import User



class ConferenceHall(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    eligible_occupancy = models.IntegerField()
    booking_days_limit = models.IntegerField()
   #image = models.ImageField(upload_to='')
    
    
class HallImage(models.Model):
    hall = models.ForeignKey(ConferenceHall,on_delete=models.SET_NULL, null=True)                
    image = models.ImageField(upload_to='halls')


class Booking(models.Model):
    employee = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,related_name="employeeId")
    employee_details = models.ForeignKey(User_details,on_delete=models.SET_NULL, null=True,related_name="detailsId")
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    participants_count = models.IntegerField()
    hall = models.ForeignKey(ConferenceHall,on_delete=models.SET_NULL, null=True,related_name="ConferenceHall")
    purpose = models.CharField(max_length=200)
    employee_remark = models.CharField(max_length=400)
    submit_date = models.DateTimeField(auto_now_add=True)
    
    hod = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,related_name="hodId")
    hod_remark = models.CharField(max_length=400)
    hod_approval_status =models.BooleanField(null=True)
    hod_status_date = models.DateTimeField(null=True)
    
    ao = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,related_name="aoId")
    ao_remark = models.CharField(max_length=400)
    ao_approval_status = models.BooleanField(null=True)
    ao_status_date = models.DateTimeField(null=True)
    
class Homepage(models.Model):
    role = models.CharField(max_length=20)
    field = models.CharField(max_length=50)
    route = models.CharField(max_length=100)
    
    
# class Booking(models.Model):
#     employee = models.ForeignKey(User,on_delete=None,related_name="employeeId")
#     employee_details = models.ForeignKey(Employee_details,on_delete=None,related_name="detailsId")
#     from_date = models.DateField()
#     time = models.TimeField()
#     to_date = models.DateField
#     time = models.TimeField
#     participants_count = models.IntegerField
#     hall = models.ForeignKey(ConferenceHall,on_delete=None,null=True,related_name="ConferenceHall")
#     purpose = models.CharField(max_length=200)
#     remark = models.CharField(max_length=400)
#     submitDateTime = models.DateTimeField(auto_now_add=True)
    
    
# class HODapproval(models.Model):
#     booking_details = models.ForeignKey(Booking,on_delete=None,null=True,related_name="HallBooking")
#     hod = models.ForeignKey(User,on_delete=None,null=True)
#     hod_remark = models.CharField(max_length=400)
#     approval_status =models.BooleanField()
#     status_date = models.DateTimeField()
    
# class AOapproval(models.Model):
#     booking_details = models.ForeignKey(Booking,on_delete=None,null=True)
#     hod_approval = models.ForeignKey(HODapproval,on_delete=None,null=True)
#     ao = models.ForeignKey(User,on_delete=None,null=True)
#     ao_remark = models.CharField(max_length=400)
#     approval_status = models.BooleanField()
#     status_date = models.DateTimeField()
    
    