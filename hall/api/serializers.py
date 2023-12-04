from rest_framework import serializers
from hall.models import Booking,ConferenceHall,HallImage,Homepage
from user.models import User_details
from django.contrib.auth.models import User

class HallImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = "__all__"
        
        
class ProfileSerializer(serializers.ModelSerializer):
    # department = serializers.ReadOnlyField(source='User_details.department')
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
    
        
class HallSerializer(serializers.ModelSerializer):
   
        #images =  HallImageSerializers(many=True, read_only=True)
        # uploaded_images = serializers.ListField(
        # child=serializers.ImageField(allow_empty_file=False, use_url=False),
        # write_only=True)
        
        class Meta:
            model = ConferenceHall
            fields = "__all__"

        # def create(self, validated_data):
        #     uploaded_images = validated_data.pop("uploaded_images")
        #     hall = ConferenceHall.objects.create(**validated_data)
            

        #     for image in uploaded_images:
        #         HallImage.objects.create(hall=hall, image=image)

        #     return hall
        
        
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
        fields = ['id','employee','from_date','to_date',
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
        
        



class ImageputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.CharField()

class AOHallputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    images = ImageSerializer(many=True)


class AOputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceHall
        fields = '__all__'


        

        
        
        


class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = ('id', 'image', 'status', 'hall')

class ConferenceHallSerializer(serializers.ModelSerializer):
    images = HallImageSerializer(many=True)

    class Meta:
        model = ConferenceHall
        fields = ('id', 'name', 'description', 'eligible_occupancy', 'booking_days_limit', 'images')

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])

        existing_image_ids = set(instance.images.values_list('id', flat=True))
        new_image_ids = {image_data.get('id', None) for image_data in images_data}

        ids_to_disable = existing_image_ids - new_image_ids
        ids_to_create = new_image_ids - existing_image_ids

        for image_data in images_data:
            image_id = image_data.get('id', None)
            if image_id in existing_image_ids:
                image_instance = HallImage.objects.get(id=image_id, hall=instance)
                image_instance.image = image_data.get('image', image_instance.image)
                image_instance.status = image_data.get('status', image_instance.status)
                image_instance.save()
            elif image_id in ids_to_disable:
                HallImage.objects.filter(id=image_id, hall=instance).update(status=False)

        for image_id in ids_to_create:
            image_data = next(data for data in images_data if data.get('id') == image_id)
            HallImage.objects.create(hall=instance, **image_data)

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.eligible_occupancy = validated_data.get('eligible_occupancy', instance.eligible_occupancy)
        instance.booking_days_limit = validated_data.get('booking_days_limit', instance.booking_days_limit)
        instance.save()

        return instance
