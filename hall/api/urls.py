from django.urls import path
from hall.api.views import AddHallAV,HODAV,AOAV,BookAV,BookingsAV


urlpatterns = [

   path('add/', AddHallAV.as_view(), name='add-hall'),
   path('booking/', BookAV.as_view(), name='new-booking'),
   path('hod<int:pk>/', HODAV.as_view(), name='HOD-approval'),
   path('ao<int:pk>/', AOAV.as_view(), name='AO-approval'),
   path('book/', BookingsAV.as_view(), name='new-bookings'),
    
    
]

