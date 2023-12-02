from rest_framework import serializers
from hall.models import Booking,ConferenceHall,HallImage,Homepage
from user.models import User_details

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
        
        
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = ['field','role','route']
        
          
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceHall
        fields = ['id','name','description']
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = ['id','image']
    
        
class AOHallSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,read_only=True,allow_null=True)
    class Meta:
        model = ConferenceHall
        fields = ['id','name','description','images']
        
    def update(self, validated_data):
        images_data = validated_data.pop('images')
        hall = ConferenceHall.objects.update(**validated_data)
        for image_data in images_data:
             HallImage.objects.update(hall=hall, **image_data)
        return hall
        
    
class BookingSerializer(serializers.ModelSerializer):
    employee_details = serializers.ReadOnlyField(source='employee_details.department')
    
    class Meta:
        model = Booking
        fields = ['employee','from_date','to_date',
                  'participants_count','hall','purpose','employee_remark','employee_details']
 
 
        
# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User_details
#         fields = ['department']
               
# class AOBookingSerializer(serializers.ModelSerializer):
#     user_details_id = serializers.RelatedField(many=True)
#     class Meta:
#         model = Booking
#         fields = ['employee','from_date','to_date',
#                   'participants_count','hall','purpose','hod_approval_status',
#                   'hod_remark','employee_remark','hod_status_date','submit_date','user_deatails_id']
        
class AOBookingSerializer(serializers.ModelSerializer):
    employee_details = serializers.ReadOnlyField(source='employee_details.department')
    employee = serializers.ReadOnlyField(source='employee.first_name')
    hall = serializers.ReadOnlyField(source='hall.name')
    submit_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    hod_status_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    from_date = serializers.DateTimeField(read_only=True,format="%Y-%m-%dT%H:%M:%S")
    to_date = serializers.DateTimeField(read_only=True,format="%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = Booking
        fields = ['employee','from_date','to_date',
                  'participants_count','hall','purpose','hod_approval_status',
                  'hod_remark','employee_remark','hod_status_date','submit_date','employee_details']

    
   
        
class HODSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['hod_remark','hod_approval_status']
        
        
class AOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['ao_remark','ao_approval_status']
        
        






        

        