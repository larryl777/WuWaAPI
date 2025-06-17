from rest_framework import serializers
from .models import CharacterStats

class CharacterSerializer(serializers.ModelSerializer): #seralize Characters (need to do for weapons, etc)
    final_stats = serializers.SerializerMethodField()

    class Meta:
        model = CharacterStats
        fields = '__all__'
    
    def get_final_stats(self, obj):
        req = self.context.get('request')
        # print("DEBUG: Request in context?", req)

        if req is None: 
           return obj.getfinalStats(include_traces= False)
        else: 
            include_traces = req.GET.get('include_traces', 'true').lower() == 'true'
            return obj.getfinalStats(include_traces)