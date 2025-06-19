from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CharacterStats, weaponStats
from .serializer import CharacterSerializer, weaponSeralizer

#character api view
@api_view(['GET'])
def get_Character(request): #func to fetch and display character data from our POST
    characters = CharacterStats.objects.all() #get all characters
    #add context to send in request for True or False
    serializer = CharacterSerializer(characters, many = True, context={'request': request}) #returns a list of data
    return Response(serializer.data)

@api_view(['POST'])
def create_Character(request): #func to send/add character data/info
    serializer = CharacterSerializer(data = request.data)
    if serializer.is_valid(): #check valid data, save it, return the data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#weapon api views
@api_view(['GET'])
def get_Weapon(request): #func to fetch and display character data from our POST
    weapons = weaponStats.objects.all() #get all characters
    #add context to send in request for True or False
    serializer = weaponSeralizer(weapons, many = True, context={'request': request}) #returns a list of data
    return Response(serializer.data)

@api_view(['POST'])
def create_Weapon(request): #func to send/add character data/info
    serializer = weaponSeralizer(data = request.data)
    if serializer.is_valid(): #check valid data, save it, return the data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE']) 
#Add a PUT and DELETE to update info (though may not actually need to delete and update for purpose of this API)
