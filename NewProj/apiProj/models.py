from django.db import models

# Create your models here.
class CharacterStats(models.Model):
    name = models.CharField(max_length = 100) #can limit name
    element = models.CharField(max_length = 100)
    weapon = models.CharField(max_length = 100)
    rarity = models.IntegerField()
    HP = models.IntegerField()
    ATK = models.IntegerField()
    DEF = models.IntegerField()
    ER = models.IntegerField(default= 100)
    critRate = models.IntegerField(default= 5)
    critDMG = models.IntegerField(default= 150)
    #storing image as just the file path since images will be added to repository
    image = models.CharField(max_length=200, blank=True, null = True)


    def __str__(self):
        return self.name 
