from django.urls import path
from .views import get_Character, create_Character

#api endpoint/path/route - getting the request
urlpatterns = [
    path('characters/', get_Character, name = 'get_Character'),
    path('characters/create', create_Character, name = 'create_Character'),
    # path('characters/<int:pk>', character_Details, name= 'character_Details')
] 