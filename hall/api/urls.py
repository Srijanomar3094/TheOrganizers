from django.urls import path
from hall.api.views import AddHallGV,HallOptionsAV,HODAV,AOAV,EmployeeBookAV,HODBookingsAV,AOBookingsAV,HomeAV,HallAV#,hall_detail
#from hall.api.views import views


urlpatterns = [

   path('add/', AddHallGV.as_view(), name='add-hall'),
   path('options/', HallOptionsAV.as_view(), name='hall-options'),
   path('home/', HomeAV.as_view(), name='left-panel'),
   path('booking/', EmployeeBookAV.as_view(), name='new-booking'),
   path('hod<int:pk>/', HODAV.as_view(), name='HOD-approval'),
   path('ao<int:pk>/', AOAV.as_view(), name='AO-approval'),
   path('hodbooked/', HODBookingsAV.as_view(), name='new-bookings'),
   path('hodbookings/', HODBookingsAV.as_view(), name='booked'),
   path('aobooked/', AOAV.as_view(), name='new-bookings'),
   path('aobookings/', AOBookingsAV.as_view(), name='booked'),
   path('hallavailable/', AOBookingsAV.as_view(), name='booked'),
   path('aohalls<int:pk>/',HallAV.as_view(),name='hall-details'),
  # path('hall/<int:pk>/', views.hall_detail),
    
    
]

