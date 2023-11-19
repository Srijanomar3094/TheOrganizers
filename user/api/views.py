from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from user.api.serializers import RegistrationSerializer


# @api_view(['POST',])
# def logout_view(request):

#     if request.method == 'POST':
#         request.user.auth_token.delete()
        
#         token = RefreshToken(base64_encoded_token_string)
#         token.blacklist()
#         return Response(status=status.HTTP_200_OK)
    
# class BlacklistRefreshView(APIView):
#     def post(self, request)
    
@api_view(['POST',])
def BlacklistRefreshView(request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")


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
            
            
            



