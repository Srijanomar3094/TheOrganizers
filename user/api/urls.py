from django.urls import path
from user.api.views import (registration_view,
                            BlacklistRefreshView)

from rest_framework_simplejwt.views import (TokenRefreshView,
                                            TokenBlacklistView,)

from .views import TokenObtainPairView

urlpatterns = [
    path('api/login_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', registration_view, name='register'),
    path('api/logout/', BlacklistRefreshView, name="logout"),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]



