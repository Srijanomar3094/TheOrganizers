from rest_framework import serializers
from hall.models import Booking,ConferenceHall


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceHall
        fields = "__all__"
        
        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceHall
        fields = ['name','description','image']
        
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['employee','from_date','to_date',
                  'participants_count','hall','purpose',
                  'employee_remark']
        
class AOBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['employee','from_date','to_date',
                  'participants_count','hall','purpose','hod_approval_status',
                  'hod_remark','employee_remark']
        
class HODSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['hod_remark','hod_approval_status']
        
        
class AOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['ao_remark','ao_approval_status']

        

        