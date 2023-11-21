from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from hall.models import Booking,ConferenceHall
from hall.api.serializers import (BookingSerializer,
                                  HallSerializer,
                                  HODSerializer,
                                  AOSerializer)
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Authenticated'}
        return Response(content)
    




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
        
        
class AddHallGV(generics.ListCreateAPIView):
    queryset = ConferenceHall.objects.all()
    serializer_class = HallSerializer
        
        
@api_view(['GET', 'POST'])

def new_booking(request):

    if request.method == 'GET':
            movies = Booking.objects.all()
            serializer = BookingSerializer(movies, many=True)
            return Response(serializer.data)
       

    if request.method == 'POST':
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
            
            
class BookAV(APIView):

   

    def get(self, request, pk):
        try:
            book = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Booking.objects.get(pk=pk)
        serializer = HODSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class HODGV(generics.UpdateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = HODSerializer




class HODAV(APIView):

   

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
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class AOAV(APIView):
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
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        
        
