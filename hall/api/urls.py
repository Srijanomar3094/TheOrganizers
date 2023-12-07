from django.urls import path
from hall.api.views import AddHallGV,HallOptionsAV,HODAV,AOAV,EmployeeBookAV,HODBookingsAV,AOBookingsAV,HomeAV,HallAV,ProfileAV,ConferenceHallUpdateView,AOBookedAV,HODBookedAV,UpdateConferenceHallView,HODAllBookingsAV#,hall_detail
#from hall.api.views import views


urlpatterns = [

   path('add/', AddHallGV.as_view(), name='add-hall'),
   path('profile/', ProfileAV.as_view(), name='add-hall'),
   path('options/', HallOptionsAV.as_view(), name='hall-options'),
   path('home/', HomeAV.as_view(), name='left-panel'),
   path('booking/', EmployeeBookAV.as_view(), name='new-booking'),
   
   
   path('hod/<int:pk>/', HODAV.as_view(), name='HOD-approval'),
   path('hodbookings/', HODBookingsAV.as_view(), name='hod-bookings'),
   path('hodbooked/', HODBookedAV.as_view(), name='hod-booked'),
   path('hodallbookings/',HODAllBookingsAV.as_view(),name='hod-all-bookings'),
   
   
   path('ao/<int:pk>/', AOAV.as_view(), name='AO-approval'),
   path('aobookings/', AOBookingsAV.as_view(), name='new-bookings'),
   path('aobooked/', AOBookedAV.as_view(), name='booked'),
   path('aohalls/',HallAV.as_view(),name='hall-details'),
   
   path('hallavailable/', AOBookingsAV.as_view(), name='booked'),
   
  # path('hall/<int:pk>/', views.hall_detail),
  # path('conference-hall/<int:pk>/', ConferenceHallUpdateView.as_view(), name='conference-hall-update'),

   path('conference-hall/<int:pk>/', UpdateConferenceHallView.as_view(), name='update_conference_hall'),
   
    
]

