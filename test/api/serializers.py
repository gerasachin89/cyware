from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class add_user_Serializer(serializers.ModelSerializer):
    first_name= serializers.RegexField(regex=r'^[a-zA-Z -.\'\_]+$', required=True, error_messages= {"invalid" : 'Please enter a valid name'})
    last_name= serializers.RegexField(regex=r'^[a-zA-Z -.\'\_]+$', required=True, error_messages= {"invalid" : 'Please enter a valid name'})
    username=serializers.CharField()

    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'},
        error_messages={
            "blank": "Password cannot be empty",
        }
    )
    class Meta:
        model=User
        fields=('username','password','first_name','last_name')
    # This method Validate the user
    def validate(self, data):
        user=data['username']
        if  user:
            if(User.objects.filter(username = user)):
                    print("in email--",user)
                    raise serializers.ValidationError({"user ":"user already exists"})
        return data
    # This method create a new User
    def create(self, validated_data):
        user_obj = User.objects.create_user(username=validated_data['username'],
                         password =validated_data['password'],
                         first_name=validated_data['first_name'],
                          last_name=validated_data['last_name'],
                         )
        return user_obj
