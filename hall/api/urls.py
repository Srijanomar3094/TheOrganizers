from django.urls import path
from hall.api.views import AddHallGV,new_booking,HODAV,AOAV,HelloView


urlpatterns = [

   path('add/', AddHallGV.as_view(), name='add-hall'),
   path('booking/', new_booking, name='new-booking'),
   path('hod<int:pk>/', HODAV.as_view(), name='HOD-approval'),
   path('ao<int:pk>/', AOAV.as_view(), name='AO-approval'),
   path('hello/', HelloView.as_view(), name='hello'),
    
    
]

