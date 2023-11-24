from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from hall.models import Booking,ConferenceHall
from user.models import User_details
from hall.api.serializers import (BookingSerializer,
                                  AOBookingSerializer,
                                  HallSerializer,
                                  HODSerializer,
                                  OptionSerializer,
                                  AOSerializer)
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
    
    
class BookAV(APIView):
    
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
            details=User_details.objects.get(employee=user_id)
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
            new = Booking.objects.filter(hod_approval_status__isnull=True)
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
        

    
class AOAV(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            try:
                book = Booking.objects.get(pk=pk)
            except Booking.DoesNotExist:
                return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = AOSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})

    def put(self, request, pk):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            movie = Booking.objects.get(pk=pk)
            serializer = AOSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save(ao=self.request.user,ao_status_date=datetime.now())
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"not permitted"})

class AOBookingsAV(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if User_details.objects.filter(user=self.request.user,role="ao").exists():
            new = Booking.objects.filter(ao_approval_status__isnull=True)
            serializer = AOBookingSerializer(new, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"not permitted"})
        
        
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