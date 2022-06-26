from skyrim.data.models import Character, Beast, Blow, Race, Place
from django.contrib.auth.models import User

def create_beast(character_name, race_type_id, health_points, id_client,id_blow,place_id_list):
    race_type = Race.objects.get(id = race_type_id)
    client = User.objects.get(id = id_client)
    character = Character(
        character_name = character_name,
        race_type = race_type,
        health_points = health_points,
        id_client = client
        )
    character.save()

    blow = Blow.objects.get(id_blow = id_blow)
    place = Place.objects.filter(id__in = place_id_list)
    beast = Beast(id_character = character,
                id_attack = blow)
    beast.save()
    beast.place.add(*place)
