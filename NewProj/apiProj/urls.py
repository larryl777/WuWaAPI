from django.urls import path
from .views import get_Character, create_Character, get_Weapon, create_Weapon

#api endpoint/path/route - getting the request
urlpatterns = [
    path('characters/', get_Character, name = 'get_Character'),
    path('characters/create', create_Character, name = 'create_Character'),
    path('weapons/', get_Weapon, name = "get_Weapon"),
    path('weapons/create', create_Weapon, name = "create_Weapon")

    # path('characters/<int:pk>', character_Details, name= 'character_Details')
] 