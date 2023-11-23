from django.urls import path
from hall.api.views import AddHallAV,HallOptionsAV,HODAV,AOAV,BookAV,HODBookingsAV,AOBookingsAV


urlpatterns = [

   path('add/', AddHallAV.as_view(), name='add-hall'),
   path('options/', HallOptionsAV.as_view(), name='hall-options'),
   path('booking/', BookAV.as_view(), name='new-booking'),
   path('hod<int:pk>/', HODAV.as_view(), name='HOD-approval'),
   path('ao<int:pk>/', AOAV.as_view(), name='AO-approval'),
   path('hodbook/', HODBookingsAV.as_view(), name='new-bookings'),
   path('aobook/', AOBookingsAV.as_view(), name='new-bookings'),
    
    
]

