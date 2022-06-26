from skyrim.data.models import BattleCharacter, Battle, Character, Place, Winner

def register_characters_in_battle_from_id(id_battle, characters_id):
    battle = Battle.objects.get(id = id_battle)
    characters_id = list(set(characters_id))
    character_list = []
    for id in characters_id:
        character = Character.objects.get(id = id)
        character_list.append(character)
    register_character_in_battle(battle,character_list)

def register_character_in_battle(battle,character_list):
    battle.fighters.add(*character_list)

def remove_character_in_battle_from_id(id_battle, character_id_list):
    battle = Battle.objects.get(id = id_battle)
    characters_id = list(set(character_id_list))
    character_list = []
    for id in characters_id:
        character = Character.objects.get(id = id)
        character_list.append(character)
    remove_character_in_battle(battle,character_list)

def remove_character_in_battle(battle, character_list):
    battle.fighters.remove(*character_list)


def set_winner_from_id(id_battle,character_id):
    battle = Battle.objects.get(id = id_battle)
    character = Character.objects.get(id = character_id)
    set_winner(battle,character)

def set_winner(battle,character):
    w = Winner(id_battle = battle, winner = character)
    w.save()

def create_battle(place_id,date,time):
    place = Place.objects.get(id = place_id)
    b = Battle(place = place,date = date, time = time)
    b.save()
    return b.id


