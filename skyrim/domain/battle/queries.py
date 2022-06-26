from unittest import result
from skyrim.data.models import BattleCharacter, Battle
from skyrim.domain.character.classes import Character_for_Battle

def get_battle(id_battle):
    battle = Battle.objects.get()
    result = {}
    result['place_id']  = battle.place.id
    result['date']  = battle.date
    result['time']  = battle.time
    return result
    

def get_characters_from_battle(id_battle):
    character_list = BattleCharacter.objects.filter(battle__id = id_battle)
    result = []
    for character in character_list:
        result.append(Character_for_Battle(character_obj= character))
    return result
