from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from hall.models import Booking,ConferenceHall,Homepage,HallImage
from user.models import User_details
from hall.api.serializers import (BookingSerializer,
                                  HomeSerializer,
                                  AOBookingSerializer,HallSerializer,ProfileSerializer,AOUpdateSerializer,AOSerializer,ALLBookingGetSerializer,NewBookingGetSerializer,
                                  HODSerializer, OptionSerializer,AOputSerializer,ConferenceHallSerializer,BookingsGetSerializer,NewHallUpdateSerializer,
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



    
    
 


        
class AddHallGV(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = HallSerializer
    
    

    
class ProfileAV(APIView):
   # permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="employee").exists():
            print(self.request.user.id)
            new = User_details.objects.filter(user=self.request.user.id)
            print(new)
            serializer = ProfileSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
    
  
  
class HallOptionsAV(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="employee").exists():
            new = ConferenceHall.objects.all()
            serializer = OptionSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
            
    
class HallAV(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            
            serializer = AOHallSerializer(many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        

        

    # def put(self, request, pk):
        
    #     if User_details.objects.filter(user=self.request.user, role="ao").exists():
    #         try:
    #             booking = ConferenceHall.objects.get(pk=pk)
    #         except ConferenceHall.DoesNotExist:
    #             return Response({"error": "Booking not found"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
    #         serializer = HallSerializer(booking, data=request.data)

    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({"error": "Not permitted"}, status=status.HTTP_403_FORBIDDEN)
        
        
    
    
    
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
            serializer = BookingsGetSerializer(new, many=True)
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
                
                
                return Response({"message":"booked"})
            else:
                return Response(serializer.errors)
        else:
            return Response({"error":"not permitted"})
        

    

class HODBookingsAV(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="hod").exists():
            new = Booking.objects.filter(hod_approval_status__isnull=True).all()
            serializer = NewBookingGetSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
        
class HODAllBookingsAV(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="hod").exists():
            new = Booking.objects.filter(hod_approval_status__isnull=False).all()
            serializer = ALLBookingGetSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
        
class HODBookedAV(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="hod").exists():
            new = Booking.objects.filter(hod_approval_status=True).all()
            serializer = BookingsGetSerializer(new, many=True)
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
                return Response({'error': 'Not found'}, status=status.HTTP_406_NOT_ACCEPTABLE)

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
            new = Booking.objects.filter(ao_approval_status__isnull=True,hod_approval_status=True).all()
            serializer = AOBookingSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
class AOBookedAV(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            new = Booking.objects.filter(ao_approval_status=True,hod_approval_status=True).all()
            serializer = AOBookingSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
         
class AOAV(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            try:
                book = Booking.objects.get(pk=pk,hod_approval_status=True)
            except Booking.DoesNotExist:
                return Response({'error': 'Not found'}, status=status.HTTP_406_NOT_ACCEPTABLE)

            serializer = AOputSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})

    def put(self, request, pk):
        if User_details.objects.filter(user=self.request.user, role="ao").exists():
            try:
                booking = Booking.objects.get(pk=pk)
            except Booking.DoesNotExist:
                return Response({"error": "Booking not found"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            serializer = AOSerializer(booking, data=request.data)

            if serializer.is_valid():
                serializer.save(ao=self.request.user,ao_status_date=datetime.now())
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Not permitted"}, status=status.HTTP_403_FORBIDDEN)



    
    
class HallDetailAV(APIView):

    def put(request, pk):
        
        try:
            hall = ConferenceHall.objects.get(pk=pk)
        except ConferenceHall.DoesNotExist:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        serializer = AOHallSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(request,pk):
        try:
            hall = ConferenceHall.objects.get(pk=pk)
        except ConferenceHall.DoesNotExist:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        serializer = HallSerializer(hall)
        return Response(serializer.data)

      


class UpdateConferenceHallView(APIView):
    def get_queryset(self, pk):
        return ConferenceHall.objects.filter(pk=pk)

    def get_object(self, pk):
        try:
            return self.get_queryset(pk).get()
        except ConferenceHall.DoesNotExist:
            return None

    def put(self, request, pk, format=None):
        hall = self.get_object(pk)

        if hall is None:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = NewHallUpdateSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            image_ids = [int(id) for id in request.data.get('image_ids', [])]
            print(image_ids)
            for image in hall.images.all():
                image.status = image.id in image_ids
                image.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


# class Update(APIView):
    
    
#     def get_queryset(self, pk):
#         return ConferenceHall.objects.filter(pk=pk)

#     def get_object(self, pk):
#         try:
#             return self.get_queryset(pk).get()
#         except ConferenceHall.DoesNotExist:
#             return None

#     def put(self, request, pk, format=None):
#         hall = self.get_object(pk)

#         if hall is None:
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

#         serializer = NewHallUpdateSerializer(hall, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             image_ids = [int(id) for id in request.data.get('image_ids', [])]
#             print(image_ids)
#             for image in hall.images.all():
#                 image.status = image.id in image_ids
#                 image.save()

#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
   



























# class ConferenceHallUpdateView(generics.UpdateAPIView):
#     queryset = ConferenceHall.objects.all()
#     serializer_class = ConferenceHallSerializer

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)           
#         self.perform_update(serializer)
#         return Response(serializer.data)
    
    
    
    #  def put(self, request, pk):
    #     movie = WatchList.objects.get(pk=pk)
    #     serializer = WatchListSerializer(movie, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ConferenceHallUpdateView(APIView):
#     queryset = ConferenceHall.objects.all()
#     serializer_class = AOUpdateSerializer
#     parser_class = [MultiPartParser, FormParser]

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         imageids=instance.pop("imageids")
#         hallid=instance.pop("hall")
#         for imageid in imageids:
        
#             HallImage.objects.filter(hall=hallid).exclude(id=imageid).update(status=False)
#             if HallImage.objects.filter(id=imageid,hall=hallid).exists():
#                 pass
#             else:
#                 AOUpdateSerializer.save(status=True)
            
            
 

class ConferenceHallUpdateView(APIView):
    def get_object(self, pk):
        try:
            return ConferenceHall.objects.get(pk=pk)
        except ConferenceHall.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = AOUpdateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
        
    