from django.db import models



class ConferenceHall(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    eligible_occupancy = models.IntegerField()
    booking_days = models.IntegerField()
    image = models.ImageField(upload_to='')
    