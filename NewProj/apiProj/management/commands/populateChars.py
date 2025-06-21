from django.core.management.base import BaseCommand
from apiProj.models import CharacterStats


#notes: if just updating the script by adding characters, or changing eixisting character stats, 
#then just run python manage.py popualteChars (as I am just adding or modifiyng data)

#If I make actual changes to model.py - adding a new field, renaming it, changing types, or default values
#then need to run python manage.py makemigrations -> python manage.py migrate -> run script

class Command(BaseCommand):
    def handle(self, *args, **options):

        #delete existing data, then populate
        CharacterStats.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted existing character data'))

        characters_Data = [
            {
            'name': 'SRover',
            'element': 'Spectro',
            'weapon': 'Sword',
            'rarity': 5,
            'base_HP': 11400,
            'base_ATK': 375,
            'base_DEF': 1369,
            'trace_ATK': 12,
            'elemDMG': 12
            
            # 'image_url': '/static/characters/Srover.jpg'
            },
            {
            'name': 'HRover',
            'element': 'Havoc',
            'weapon': 'Sword',
            'rarity': '5',
            'base_HP': 10825,
            'base_ATK': 413,
            'base_DEF': 1259,
            'trace_ATK': 12,
            'elemDMG': 12
            # 'image_url': '/static/characters/Hrover.jpg'
            },
            {
            'name': 'ARover',
            'element': 'Aero',
            'weapon': 'Sword',
            'rarity': '5',
            'base_HP': 10775,
            'base_ATK': 438,
            'base_DEF': 1137,
            'trace_ATK': 12,
            'healBONUS': 12
            # 'image_url': '/static/characters/Arover.jpg'
            },
        ]
        for char_data in characters_Data:
            character = CharacterStats.objects.create(**char_data)
            print(f"Created character: {character.name}")

        print(f"Successfully populated {len(characters_Data)} characters!")