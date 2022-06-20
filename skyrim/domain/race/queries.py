from skyrim.data.models import Character, Race

def get_all_races():
    result = Race.objects.all()
    return result.values()

def get_weakness_from_character_id(character_id):
    character = Character.objects.get(character_id)
    return get_weakness_from_character(character)

def get_weakness_from_character(character):
    return character.race_type.weakness.id

