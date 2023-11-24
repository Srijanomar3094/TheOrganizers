from rest_framework import serializers
from hall.models import Booking,ConferenceHall,HallImage

class HallImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = "__all__"
        
class HallSerializer(serializers.ModelSerializer):
   
        images =  HallImageSerializers(many=True, read_only=True)
        uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True)
        
        class Meta:
            model = ConferenceHall
            fields = "__all__"

        def create(self, validated_data):
            uploaded_images = validated_data.pop("uploaded_images")
            hall = ConferenceHall.objects.create(**validated_data)
            

            for image in uploaded_images:
                HallImage.objects.create(hall=hall, image=image)

            return hall
        
        
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
        
        






        

        