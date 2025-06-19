from django.core.management.base import BaseCommand
from apiProj.models import weaponStats


#notes: if just updating the script by adding characters, or changing eixisting character stats, 
#then just run python manage.py popualteChars (as I am just adding or modifiyng data)

#If I make actual changes to model.py - adding a new field, renaming it, changing types, or default values
#then need to run python manage.py makemigrations -> python manage.py migrate -> run script

class Command(BaseCommand):
    def handle(self, *args, **options):

        #delete existing data, then populate
        weaponStats.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted existing weapon data'))

        weapons_Data = [
            {
            'name': 'Emerald of Genesis',
            'type': 'Sword',
            'rarity': 5,
            'base_ATK': 587,
            
            'secondary_Stat': 'critRate',
            'secondary_Val': 24.3,
            'ER': 12.8,
            'ATK': 12,
            'dupes': 1
            
            }
        ]
        for eachWeapon in weapons_Data:
            weapon = weaponStats.objects.create(**eachWeapon)
            print(f"Created weapon: {weapon.name}")

        print(f"Successfully populated {len(weapons_Data)} +!")