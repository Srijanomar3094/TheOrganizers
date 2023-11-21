from rest_framework import serializers
from hall.models import Booking,ConferenceHall


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceHall
        fields = "__all__"
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['employee','employee_details','from_date','to_date',
                  'participants_count','hall','purpose',
                  'employee_remark']

        

        