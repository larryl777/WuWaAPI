from django.db import models

# Create your models here.
class CharacterStats(models.Model):
    name = models.CharField(max_length = 100) #can limit name
    HP = models.IntegerField()
    ATK = models.IntegerField()
    DEF = models.IntegerField()
    ER = models.IntegerField(default= 100)
    critRate = models.IntegerField(default= 5)
    critDMG = models.IntegerField(default= 150)


    def __str__(self):
        return self.name 
