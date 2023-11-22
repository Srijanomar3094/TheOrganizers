from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from hall.models import Booking,ConferenceHall
from user.models import User_details
from hall.api.serializers import (BookingSerializer,
                                  HallSerializer,
                                  HODSerializer,
                                  AOSerializer)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from datetime import datetime





class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Authenticated'}
        return Response(content)    
    

        
class AddHallGV(generics.ListCreateAPIView):
    queryset = ConferenceHall.objects.all()
    serializer_class = HallSerializer
        

            
class BookAV(APIView):
    
    

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        movies = Booking.objects.all()
        serializer = BookingSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = self.request.user
        details=User_details.objects.get(employee=user_id)
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=user_id,employee_details=details)
            
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class HODAV(APIView):

   
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        try:
            book = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HODSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Booking.objects.get(pk=pk)
        serializer = HODSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save(hod=self.request.user,hod_status_date=datetime.now())
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class AOAV(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        try:
            book = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AOSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Booking.objects.get(pk=pk)
        serializer = AOSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save(ao=self.request.user,ao_status_date=datetime.now())
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        
        
# class HODGV(generics.UpdateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = HODSerializer

# @api_view(['GET', 'POST'])
# def add_hall(request):

#     if request.method == 'GET':
#         movies = ConferenceHall.objects.all()
#         serializer = HallSerializer(movies, many=True)
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
#             movies = Booking.objects.all()
#             serializer = BookingSerializer(movies, many=True)
#             return Response(serializer.data)
       

#     if request.method == 'POST':
#             serializer = BookingSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)