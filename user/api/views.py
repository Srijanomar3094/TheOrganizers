from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from user.api.serializers import RegistrationSerializer,TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import OutstandingToken,BlacklistedToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


    
@api_view(['POST',])
def BlacklistRefreshView(request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response({"message":"Success"})


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
       
        

            refresh = RefreshToken.for_user(account)

            
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            
            return Response(data, status=status.HTTP_201_CREATED)
        
        
        else:
            data = serializer.errors
            
class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# class MyLogin(TokenObtainPairSerializer):
#     username_field = 'email'
#     def validate(self, attrs):
#         """Overrides validate method in TokenObtainPairSerializer"""
       
#         # custom login as per your requirement
#         # Here, we will check whether the user email is verified, if not return an error
#         # if not email.verified:
#         #     return Response("Please verify your email.", status=status.HTTP_400_BAD_REQUEST).data# validate the user credentials returns an error if credentials are not valid
#         data = super(TokenObtainPairSerializer, self).validate(attrs)
#         return Response("loggedin", status=status.HTTP_200_OK)
# class MyTokenObtainView(TokenObtainPairView):
#         serializer_class = MyLogin
            



