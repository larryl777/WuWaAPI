from django.core.management.base import BaseCommand
from apiProj.models import CharacterStats

class Populate(BaseCommand):
    def run(self, *args, **options):

        #delete existing data, then populate
        CharacterStats.objects.all().delete()

        characters_Data = []