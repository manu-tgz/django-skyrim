from unittest import result
from skyrim.data.models import Character, PlayerRace, Race

def get_all_races():
    result = Race.objects.all()
    return result.values()

def get_all_player_races():
    player_race_list = PlayerRace.objects.all()
    result = []
    for player_race in player_race_list:
        current = {}
        raza = player_race.id_race
        current["id"] = raza.id
        current["name"] = raza.race_name
        current["weakness_id"] = raza.weakness.id
        result.append(current)
    return result

def get_weakness_from_character_id(character_id):
    character = Character.objects.get(character_id)
    return get_weakness_from_character(character)

def get_weakness_from_character(character):
    return character.race_type.weakness.id

