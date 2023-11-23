from django.contrib.auth.models import User
from django.forms import EmailField
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response

#from hallbooking.user.models import User_details


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
    
    
class MyLogin(TokenObtainPairSerializer):
    username_field = 'email'
    
    # def validate(self, attrs):
    #     """Overrides validate method in TokenObtainPairSerializer"""
       
        # custom login as per your requirement
        # Here, we will check whether the user email is verified, if not return an error
        # if not email_field.verified:
        # #     return Response("Please verify your email.", status=status.HTTP_400_BAD_REQUEST).data# validate the user credentials returns an error if credentials are not valid
        #     data = super(TokenObtainPairSerializer, self).validate(attrs)
        #     return data
        # return Response("loggedin", status=status.HTTP_200_OK)
    
    
class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyLogin
    
    
    
    
    


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#         username_field = User.EMAIL_FIELD



# class MyTokenObtainSerializer(Serializer):
#     username_field = User.EMAIL_FIELD

#     def __init__(self, *args, **kwargs):
#         super(MyTokenObtainSerializer, self).__init__(*args, **kwargs)

#         self.fields[self.username_field] = CharField()
#         self.fields['password'] = PasswordField()

#     def validate(self, attrs):
#         # self.user = authenticate(**{
#         #     self.username_field: attrs[self.username_field],
#         #     'password': attrs['password'],
#         # })
#         self.user = User.objects.filter(email=attrs[self.username_field]).first()
#         print(self.user)

#         if not self.user:
#             raise ValidationError('The user is not valid.')

#         if self.user:
#             if not self.user.check_password(attrs['password']):
#                 raise ValidationError('Incorrect credentials.')
#         print(self.user)
        
        
#         if self.user is None or not self.user.is_active:
#             raise ValidationError('No active account found with the given credentials')

#         return {}

#     @classmethod
#     def get_token(cls, user):
#         raise NotImplemented(
#             'Must implement `get_token` method for `MyTokenObtainSerializer` subclasses')


# class MyTokenObtainPairSerializer(MyTokenObtainSerializer):
#     @classmethod
#     def get_token(cls, user):
#         return RefreshToken.for_user(user)

#     def validate(self, attrs):
#         data = super(MyTokenObtainPairSerializer, self).validate(attrs)

#         refresh = self.get_token(self.user)

#         data['refresh'] = text_type(refresh)
#         data['access'] = text_type(refresh.access_token)

#         return data
        