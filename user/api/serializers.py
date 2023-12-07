from django.contrib.auth.models import User
from django.forms import EmailField
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):


        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# class MyLogin(TokenObtainPairSerializer):
#     username_field = 'email'
    
#     # def validate(self, attrs):
#     #     """Overrides validate method in TokenObtainPairSerializer"""
       
#         # custom login as per your requirement
#         # Here, we will check whether the user email is verified, if not return an error
#         # if not email_field.verified:
#         # #     return Response("Please verify your email.", status=status.HTTP_400_BAD_REQUEST).data# validate the user credentials returns an error if credentials are not valid
#         #     data = super(TokenObtainPairSerializer, self).validate(attrs)
#         #     return data
#         # return Response("loggedin", status=status.HTTP_200_OK)
    
    
# class MyTokenObtainView(TokenObtainPairView):
#     serializer_class = MyLogin
    
    
    
    
    


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#         username_field = User.EMAIL_FIELD


