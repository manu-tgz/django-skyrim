from skyrim.data.models import BattleCharacter, Battle, Character, Winner

def insert_several_characters_same_battle(id_battle, character_ids):
    battle = Battle.objects.get(id = id_battle)
    for id in character_ids:
        character = Character.objects.get(id = id)
        BattleCharacter.objects.create(battle = battle, character = character)

def register_characters_in_battle_from_id(id_battles, characters_id):
    battle = Battle.objects.get(id = id_battles)
    characters_id = list(set(characters_id))
    character_list = []
    for id in characters_id:
        character = Character.objects.get(id = id)
        character_list.append(character)
    register_character_in_battle(battle,character_list)

def register_character_in_battle(battle,character_list):
    for character in character_list:
        BattleCharacter.objects.create(battle = battle, character = character)

def set_winner_from_id(id_battle,character_id):
    battle = Battle.objects.get(id = id_battle)
    character = Character.objects.get(id = character_id)
    set_winner(battle,character)

def set_winner(battle,character):
    Winner.objects.create(id_battle = battle, winner = character)

