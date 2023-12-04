from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from hall.models import Booking,ConferenceHall,Homepage,HallImage
from user.models import User_details
from hall.api.serializers import (BookingSerializer,
                                  HomeSerializer,
                                  AOBookingSerializer,
                                  HallSerializer,
                                  HODSerializer,
                                  OptionSerializer,
                                  AOputSerializer,
                                  ConferenceHallSerializer,
                                  ProfileSerializer,
                                  AOHallSerializer)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from datetime import datetime


        
# class AddHallGV(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = ConferenceHall.objects.all()
#     serializer_class = HallSerializer


    
    
    
# class AddHallAV(APIView):
    

#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         if User_details.objects.filter(user=self.request.user,role="ao").exists():
#             new = ConferenceHall.objects.all()
#             serializer = HallSerializer(new, many=True)
#             return Response(serializer.data)
#         else:
#             return Response({"error":"not permitted"})

#     def post(self, request):
#         if User_details.objects.filter(user=self.request.user,role="ao").exists():
#             user_id = self.request.user
#             details=User_details.objects.get(employee=user_id)
#             serializer = HallSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save(employee=user_id,employee_details=details)
                
                
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#         else:
#             return Response({"error":"not permitted"})  



    
    
 

class HallOptionsAV(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="employee").exists():
            new = ConferenceHall.objects.all()
            serializer = OptionSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
class AddHallGV(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = HallSerializer
    
    
    
class ProfileGV(ListAPIView):
    serializer_class = ProfileSerializer
    
    
    
class HallAV(APIView):
    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            new = ConferenceHall.objects.all()
            
            serializer = AOHallSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        

        

    def put(self, request, pk):
        
        if User_details.objects.filter(user=self.request.user, role="ao").exists():
            try:
                booking = ConferenceHall.objects.get(pk=pk)
            except ConferenceHall.DoesNotExist:
                return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = HallSerializer(booking, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Not permitted"}, status=status.HTTP_403_FORBIDDEN)
        
        
    
    
    
class HomeAV(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_role=User_details.objects.filter(user=self.request.user).first()
        if user_role.role=="employee":
            fields=Homepage.objects.filter(role="employee").values('field','role','route')
            serializer = HomeSerializer(fields, many=True)
            return Response(serializer.data)
        
        elif user_role.role=="hod":
            fields=Homepage.objects.filter(role="hod").values('field','role','route')
            serializer = HomeSerializer(fields, many=True)
            return Response(serializer.data)
     
        elif user_role.role=="ao":
            fields=Homepage.objects.filter(role="ao").values('field','role','route')
            serializer = HomeSerializer(fields, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
         
class EmployeeBookAV(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="employee").exists():
            new = Booking.objects.all()
            serializer = BookingSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})

    def post(self, request):
        if User_details.objects.filter(user=self.request.user,role="employee").exists():
            user_id = self.request.user
            details=User_details.objects.get(user_id=user_id)
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(employee=user_id,employee_details=details)
                
                
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({"error":"not permitted"})
        

    

class HODBookingsAV(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="hod").exists():
            new = Booking.objects.filter(hod_approval_status__isnull=True).all()
            serializer = BookingSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})


class HODAV(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        if User_details.objects.filter(user=self.request.user,role="hod").exists():
            try:
                book = Booking.objects.get(pk=pk)
            except Booking.DoesNotExist:
                return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = HODSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})

    def put(self, request, pk):
        if User_details.objects.filter(user=self.request.user,role="hod").exists():
            movie = Booking.objects.get(pk=pk)
            serializer = HODSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save(hod=self.request.user,hod_status_date=datetime.now())
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"not permitted"})
        

class AOBookingsAV(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            new = Booking.objects.filter(ao_approval_status__isnull=True).all()
            serializer = AOBookingSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
         
class AOAV(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            try:
                book = Booking.objects.get(pk=pk)
            except Booking.DoesNotExist:
                return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = AOputSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})

    def put(self, request, pk):
        if User_details.objects.filter(user=self.request.user, role="ao").exists():
            try:
                booking = Booking.objects.get(pk=pk)
            except Booking.DoesNotExist:
                return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = AOputSerializer(booking, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Not permitted"}, status=status.HTTP_403_FORBIDDEN)



        
# class HODGV(generics.UpdateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = HODSerializer

# @api_view(['GET', 'POST'])
# def add_hall(request):

#     if request.method == 'GET':
#         new = ConferenceHall.objects.all()
#         serializer = HallSerializer(new, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = HallSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


        
# @api_view(['GET', 'POST'])

# def new_booking(request):

#     if request.method == 'GET':
#             new = Booking.objects.all()
#             serializer = BookingSerializer(new, many=True)
#             return Response(serializer.data)
       

#     if request.method == 'POST':
#             serializer = BookingSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
# class AO(APIView):
    
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         if roomAvailable(validated_data):
#                     ...
#                     instance.save()
#                 else:
#                     raise serializers.ValidationError({
#                         "detail": "Room is not available for these dates."
#                     })
#                 return instance
# def hallAvailableAV(validated_data):
#     ...

#     bookings = Booking.exclude(
#         booked_for_datetime__date__gt=validated_data['booked_till_datetime'],
#     ).exclude(
#         booked_till_datetime__date__lt=validated_data['booked_for_datetime'],
#     )

   # return not bookings.exists()
   
   
   
   
#    def update(self, instance, validated_data):
#         contacts_data = validated_data.pop('contacts')

#         instance.name = validated_data.get('name', instance.name)
#         instance.save()

#         # many contacts
#         for contact_data in contacts_data:
#             contact = Contact.objects.get(pk=contact_data['id']) # this will crash if the id is invalid though
#             contact.name = contact_data.get('name', contact.name)
#             contact.last_name = contact_data.get('last_name', contact.last_name)
#             contact.save()

#         return instance
    
    
    
    
#     def update(self, instance, validated_data):
#         images_data = validated_data.pop('images')

#         instance.name = validated_data.get('name', instance.name)
#         instance.save()

#         # many contacts
#         for image_data in images_data:
#             image = HallImage.objects.get(pk=image_data['id']) # this will crash if the id is invalid though
#             image.image = contact_data.get('name', contact.name)
#             contact.last_name = contact_data.get('last_name', contact.last_name)
#             contact.save()

#         return instance
    
    
    
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET', 'PUT'])
def hall_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        hall = ConferenceHall.objects.get(pk=pk)
    except ConferenceHall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HallSerializer(hall)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AOHallSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#     @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ConferenceHallUpdateView(generics.UpdateAPIView):
    queryset = ConferenceHall.objects.all()
    serializer_class = ConferenceHallSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
