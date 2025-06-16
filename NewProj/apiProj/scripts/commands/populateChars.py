from django.core.management.base import BaseCommand
from apiProj.models import CharacterStats

class Populate(BaseCommand):
    def run(self, *args, **options):

        #delete existing data, then populate
        CharacterStats.objects.all().delete()

        characters_Data = [
            {
            'name': 'SRover',
            'element': 'Spectro',
            'weapon': 'Sword',
            'rarity': '5',
            'HP': 11400,
            'ATK': 375,
            'DEF': 1369,
            'image_url': '/static/characters/Srover.jpg'
            },
                        {
            'name': 'HRover',
            'element': 'Havoc',
            'weapon': 'Sword',
            'rarity': '5',
            'HP': 10825,
            'ATK': 413,
            'DEF': 1259,
            'image_url': '/static/characters/Hrover.jpg'
            },
                        {
            'name': 'ARover',
            'element': 'Aero',
            'weapon': 'Sword',
            'rarity': '5',
            'HP': 10775,
            'ATK': 438,
            'DEF': 1136,
            'image_url': '/static/characters/Arover.jpg'
            },
        ]