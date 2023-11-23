from django.urls import path
from user.api.views import (registration_view,
                            BlacklistRefreshView,LogoutAllView)

from rest_framework_simplejwt.views import (TokenRefreshView,
                                            TokenBlacklistView)
from .serializers import MyTokenObtainView


urlpatterns = [
    path('api/login_token/', MyTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', registration_view, name='register'),
    path('api/logout/', BlacklistRefreshView, name="logout"),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('token/logout/', LogoutAllView.as_view(), name='logout view'),
  #  path('api/login/', MyLogin, name='login view'),
]



