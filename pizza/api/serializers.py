from django.db.models import fields
from rest_framework import serializers
from .models import *

#List containing all the allowed pizza types
type_allowed = ['Regular','Square']

#List containing all the allowed pizza types
size_allowed = ['Small','Medium','Large']


class pizzaSerializers(serializers.ModelSerializer):
    
    #Function to check if the entered type of piza is correct or not
    def validate_type(self, value):
        if value not in type_allowed:
            raise serializers.ValidationError('Type must be : ' + ", ".join(type_allowed))
        return value

    #Function to check if the entered size of piza is correct or not
    def validate_size(self, value):
        if value not in size_allowed:
            raise serializers.ValidationError('Size must be : ' + ", ".join(size_allowed))
        return value


    class Meta:
        model = Pizza
        fields = "__all__"