from rest_framework import serializers
from .models import person,team

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields =['team_name']

class personSerializer(serializers.ModelSerializer): 
    team=teamSerializer()
    team_info = serializers.SerializerMethodField()
    class Meta: 
        model = person
        fields = "__all__" 
        depth= 1

# extra field
    def get_team_info(self,obj):
        return "extra field"


# validation
    def validate(self,data):
        spl_char = "!@#%$&()|\?<>"
        if any(c in spl_char for c in data['name']):
            raise serializers.ValidationError('name should not have special character')
        if data['age']<18:
            raise serializers.ValidationError("age should not be less than 18")
        
        return data