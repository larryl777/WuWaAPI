from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CharacterStats
from .serializer import CharacterSerializer

@api_view(['GET'])
def get_Character(request): #func to fetch and display character data from our POST
    characters = CharacterStats.objects.all() #get all characters
    seralizer = CharacterSerializer(characters, many = True) #returns a list of data
    return Response(seralizer.data)

@api_view(['POST'])
def create_Character(request): #func to send/add character data/info
    serializer = CharacterSerializer(data = request.data)
    if serializer.is_valid(): #check valid data, save it, return the data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
