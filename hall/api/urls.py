from django.urls import path
from hall.api.views import AddHallGV,HODAV,AOAV,HelloView,BookAV


urlpatterns = [

   path('add/', AddHallGV.as_view(), name='add-hall'),
   path('booking/', BookAV.as_view(), name='new-booking'),
   path('hod<int:pk>/', HODAV.as_view(), name='HOD-approval'),
   path('ao<int:pk>/', AOAV.as_view(), name='AO-approval'),
   path('hello/', HelloView.as_view(), name='hello'),
    
    
]

