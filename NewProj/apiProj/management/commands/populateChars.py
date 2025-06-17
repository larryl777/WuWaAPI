from django.core.management.base import BaseCommand
from apiProj.models import CharacterStats

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
            
            # 'image_url': '/static/characters/Srover.jpg'
            },
            # {
            # 'name': 'HRover',
            # 'element': 'Havoc',
            # 'weapon': 'Sword',
            # 'rarity': '5',
            # 'HP': 10825,
            # 'ATK': 413,
            # 'DEF': 1259,
            # 'image_url': '/static/characters/Hrover.jpg'
            # },
            #             {
            # 'name': 'ARover',
            # 'element': 'Aero',
            # 'weapon': 'Sword',
            # 'rarity': '5',
            # 'HP': 10775,
            # 'ATK': 438,
            # 'DEF': 1136,
            # 'image_url': '/static/characters/Arover.jpg'
            # },
        ]
        for char_data in characters_Data:
            character = CharacterStats.objects.create(**char_data)
            print(f"Created character: {character.name}")

        print(f"Successfully populated {len(characters_Data)} characters!")