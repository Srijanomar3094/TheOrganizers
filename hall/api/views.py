from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from hall.models import Booking,ConferenceHall
from hall.api.serializers import (BookingSerializer,HallSerializer)
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def add_hall(request):

    if request.method == 'GET':
        movies = ConferenceHall.objects.all()
        serializer = HallSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
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
        
        
