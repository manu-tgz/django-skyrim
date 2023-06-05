from unittest import result
from skyrim.data.models import BattleCharacter, Battle,Event, Winner
from skyrim.domain.character.classes import Character_for_Battle
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError
from django.db.models import F, Max, Min, Sum, Subquery

def get_battle(id_battle):
    battle = Battle.objects.get(id = id_battle)
    result = {
        'place_id': battle.place.id,
        'place_name' : battle.place.place_name,
        'date' : battle.date,
        'time': battle.time,
    }
    
    return result
    

def get_characters_from_battle(id_battle):
    battle = Battle.objects.get(id = id_battle)
    battle_character_list = battle.fighters.all()
    result = []
    for item in battle_character_list:
        current = {
            'id':item.id,
            'Nombre':item.character_name,
            'Raza_label':item.race_type.race_name,
            'Raza_key':item.race_type.id,
            'Puntos_de_Vida':item.health_points,
            'Creador_label':item.id_client.username,
            'Creador_key':item.id_client.id,
        }
        result.append(current)
    return result

def get_characters_obj_from_battle(id_battle):
    battle = Battle.objects.get(id = id_battle)
    battle_character_list = battle.fighters.all()
    result = []
    for item in battle_character_list:
        result.append(Character_for_Battle(character_obj = item))
    return result

def get_winner(battle_id):
    winner = Winner.objects.get(id_battle = battle_id)
    result = {}
    result['winner_id'] = winner.winner.id
    result['name'] = winner.winner.character_name
    result['battle_id'] = winner.id_battle.id
    return result

def get_battle_stats(battle_id):
    characters_with_damage_done = Event.objects.filter(id_battle = battle_id
    ).values('id_attacker__character_name'
    ).annotate(damage_points=(Sum('health_points_before') - Sum('health_points_after')))
    min_max_damage = characters_with_damage_done.aggregate(min_damage = Min('damage_points'),max_damage = Max('damage_points'))
    most_violent = characters_with_damage_done.filter(damage_points = min_max_damage['max_damage'])
    less_violent = characters_with_damage_done.filter(damage_points = min_max_damage['min_damage'])

    characters_with_damage_recieved = Event.objects.filter(id_battle = battle_id
    ).values('id_damaged__character_name'
    ).annotate(damage_points=(Sum('health_points_before') - Sum('health_points_after')))
    min_max_damage = characters_with_damage_recieved.aggregate(min_damage = Min('damage_points'),max_damage = Max('damage_points'))
    most_damaged = characters_with_damage_recieved.filter(damage_points = min_max_damage['max_damage'])
    less_damaged = characters_with_damage_recieved.filter(damage_points = min_max_damage['min_damage'])
    return {'most_violent':most_violent,
        'less_violent':less_violent,
        'most_damaged':most_damaged,
        'less_damaged':less_damaged}

