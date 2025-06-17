from django.db import models

# Create your models here.
class CharacterStats(models.Model):
    name = models.CharField(max_length = 100) #can limit name
    element = models.CharField(max_length = 100, default = 'Temp')
    weapon = models.CharField(max_length = 100, default = 'Temp')
    rarity = models.IntegerField(default = 5)
    base_HP = models.IntegerField()
    base_ATK = models.IntegerField()
    base_DEF = models.IntegerField()
    base_ER = models.FloatField(default= 100.0)
    base_critRate = models.FloatField(default= 5.0)
    base_critDMG = models.FloatField(default= 150.0)
    
    #additional stats - stat bonuses that can be changed through echoes 
    #initally set to default vals, but will be updated with PUT/PATCH request according to user's own echoes
    rSkillDMG = models.FloatField(default = 0.0)
    bATKDMG = models.FloatField(default = 0.0)
    hATKDMG = models.FloatField(default = 0.0)
    rLibDMG = models.FloatField(default = 0.0)
    elemDMG = models.FloatField(default = 0.0)
    healBONUS = models.FloatField(default = 0.0)

    #additional stats from skill tree
    trace_HP = models.FloatField(default= 0.0)
    trace_ATK = models.FloatField(default= 0.0)
    trace_DEF = models.FloatField(default= 0.0)
    trace_critRate = models.FloatField(default= 0.0)
    trace_critDMG = models.FloatField(default= 0.0)
    trace_elemDMG = models.FloatField(default= 0.0)
    trace_healBONUS= models.FloatField(default= 0.0)

    #storing image as just the file path since images will be added to repository
    # image = models.CharField(max_length=200, blank=True, null = True)

    def getfinalStats(self, include_Traces = True):
        if(include_Traces):
            final_HP = int(self.base_HP * (1 + self.trace_HP/100))
            final_ATK = int(self.base_ATK * (1 + self.trace_ATK/100))
            final_DEF = int(self.base_DEF * (1 + self.trace_DEF/100))
            final_critRate = int(self.base_critRate * (1 + self.trace_critRate/100))
            final_critDMG = int(self.base_critDMG * (1 + self.trace_critDMG/100))
            final_elemDMG = int(self.elemDMG * (1 + self.trace_elemDMG/100))

            return {
                'HP': final_HP,
                'ATK': final_ATK,
                'DEF': final_DEF,
                'ER': self.base_ER, #no ER trace skill, so just return initial
                'Crit Rate': final_critRate,
                'Crit DMG': final_critDMG,
                'elemDMG' : final_elemDMG
            }
            
        else:
            return {
                'HP': self.base_HP,
                'ATK': self.base_ATK,
                'DEF': self.base_DEF,
                'ER': self.base_ER,
                'Crit Rate': self.base_critRate,
                'Crit DMG': self.base_critDMG,
                'elemDMG': self.elemDMG
            }
        


#weapon data
# class weaponStats(models.Model):
#     name = models.CharField(max_length = 100) #can limit name
#     type = models.CharField(max_length = 100)
#     rarity = models.IntegerField()
#     base_ATK = models.IntegerField()

    
#     #secondary stat of weapons 
#     second_Stat = models.CharField(max_length= 100)
#     secondary_Val = models.FloatField(default = 0.0)

#     #passive skill stat bonuses
#     passive_ATK = models.FloatField(default = 0)
#     HP = models.FloatField(default = 0)
#     DEF = models.FloatField(default = 0)
#     ER = models.FloatField(default= 0)
#     critRate = models.FloatField(default= 0)
#     critDMG = models.FloatField(default= 0)
#     rSkillDMG = models.FloatField(default = 0)
#     bATKDMG = models.FloatField(default = 0)
#     hATKDMG = models.FloatField(default = 0)
#     rLibDMG = models.FloatField(default = 0)
#     elemDMG = models.FloatField(default = 0)
#     healBONUS = models.FloatField(default = 0)

#     #storing image as just the file path since images will be added to repository
#     image = models.CharField(max_length=200, blank=True, null = True)

#     def getfinalStats(self):
#         return self



    def __str__(self):
        return self.name 
