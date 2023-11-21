from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from hall.models import Booking,ConferenceHall
from hall.api.serializers import (BookingSerializer,
                                  HallSerializer,
                                  HODSerializer,
                                  AOSerializer)
from rest_framework.permissions import IsAuthenticated





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
        # watchlist = WatchList.objects.get(pk=pk)
        # employee = self.request.user
        
        # review_queryset = Review.objects.filter(watchlist=watchlist, review_user=employee)



        # if watchlist.number_rating == 0:
        #     watchlist.avg_rating = serializer.validated_data['rating']
        # else:
        #     watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2

        # watchlist.number_rating = watchlist.number_rating + 1
        # watchlist.save()

        # serializer.save(watchlist=watchlist, review_user=review_user)
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            id = request.user
            add = Booking.objects.filter()
            serializer.save()
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
            serializer.save()
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
            serializer.save()
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