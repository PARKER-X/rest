from dataclasses import fields
import imp
from operator import imod
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user




class studentserializers(serializers.ModelSerializer):

    class Meta:
        model = student
        # fields = ['name','age']
        # exclude = ['']
        fields ="__all__"


    def validate(self, data):
        if 'age' in data and  data['age'] < 18:
            raise serializers.ValidationError({'error' : "age cannot be less than 18"})
        
        if 'name' in data and  data['name'].isalpha() == False:
            raise serializers.ValidationError({'error' : "No digit allowed"})
        return data
    

class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ="__all__"


class Bookserializers(serializers.ModelSerializer):
    category = Categoryserializers()
    class Meta:
        model = Book
        fields ="__all__"
