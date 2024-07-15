from rest_framework import serializers
from .models import person

class personSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = person
        fields = "__all__" 

    def validate(self,data):
        spl_char = "!@#%$&()|\?<>"
        if any(c in spl_char for c in data['name']):
            raise serializers.ValidationError('name should not have special character')
        if data['age']<18:
            raise serializers.ValidationError("age should not be less than 18")
        
        return data