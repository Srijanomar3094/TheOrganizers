from django.urls import path
from hall.api.views import add_hall,new_booking


urlpatterns = [

   path('add/', add_hall, name='add-hall'),
   path('booking/', new_booking, name='new-booking'),
    
    
]

