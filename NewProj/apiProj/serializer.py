from rest_framework import serializers
from .models import CharacterStats

class CharacterSerializer(serializers.ModelSerializer): #seralize Characters (need to do for weapons, etc)
    class Meta:
        model = CharacterStats
        fields = '__all__'
    
    def getCharacterStats(self, obj):
        req = self.context.get('request')
        if req is None: 
            return 
        else: 
            include_Traces = req.GET.get('include_Traces', 'true').lower() == 'true'
            return obj.getFinalStats(include_Traces)