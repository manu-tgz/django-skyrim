from skyrim.data.models import Character, Player, Race
from django.contrib.auth.models import User

def create_player(character_name,race_type_id,health_points,id_client):
    race_type = Race.objects.get(id = race_type_id)
    user = User.objects.get(id = id_client)
    character = Character(
        character_name = character_name,
        race_type = race_type,
        health_points = health_points,
        id_client = user
    )
    character.save()
    player = Player(id_character = character)
    player.save()
    return player.id