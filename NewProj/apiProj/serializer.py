from rest_framework import serializers
from .models import CharacterStats

class CharacterSerializer(serializers.ModelSerializer): #seralize Characters (need to do for weapons, etc)
    class Meta:
        model = CharacterStats
        fields = '__all__'