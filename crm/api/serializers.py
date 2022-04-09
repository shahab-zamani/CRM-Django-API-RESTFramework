from rest_framework import serializers
from .models import Leads
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class LeadsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ['id','firstName','lastName','email','company','phoneNumber','mobileNumber','jobPosition']


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email']

        extra_kwargs = {'password':{
            'write_only' : True,
            'required' : True

        }

        }

    def create (self , validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user












    # default serializer
    #firstName = serializers.CharField(max_length=30)
   # lastName = serializers.CharField(max_length=30)
   # email = serializers.CharField(max_length=30)
  #  phoneNumber = serializers.CharField(max_length=30)
   # company = serializers.CharField(max_length=30)
   # jobPosition = serializers.CharField(max_length=30)
   # mobileNumber = serializers.CharField(max_length=30)




    #def create(self, validated_data):
        #return Leads.objects.create(validated_data)
    #def update(self, instance, validated_data):

        #instance.firstName = validated_data.get ('firstName' , instance.firstName)
       # instance.lastName = validated_data.get('lastName', instance.lastName)

