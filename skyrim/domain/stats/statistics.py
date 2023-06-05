from django.db.models import F, Count, Sum, Value
from skyrim.data.models import Battle

from skyrim.data import models

def Beast_List():
    return models.BattleCharacter.objects.values('character__race_type__race_name'
        ).annotate(count=Count('character__race_type__race_name')
        ).order_by('-count')[:10]

def Rank_n_players(n):
    return models.Winner.objects.values('winner__character_name'
        ).annotate(count=Count('winner__character_name')
        ).order_by('-count')[:n]

def BattleDuration():
    largest_battles = models.Event.objects.all().values('id_battle').annotate(count=Count('id_battle')).order_by('-count')[:10]
    content = []
    for item in largest_battles:
        battle = Battle.objects.get(id = item['id_battle']) 
        current = {
        'place_id': battle.place.id,
        'place_name' : battle.place.place_name,
        'date' : battle.date,
        'time': battle.time,}
        content.append({'duration': item, 'info':current})
         
    return content

# def Rank_n_attacks(n):
#     return models.Event.objects.values('id_attack__attack_type__type'
#     ).annotate(count=Count('id_attack')
#     ).order_by('-count')[:n]

def Rank_n_attacks(n):
    return models.Event.objects.values('id_attack','id_attack__attack_type__type','id_attack__damage_point'
    ).annotate(count=Count('id_attack')
    ).order_by('-count')[:n]

def know_spell():
    return models.KnownSpell.objects.values('id_spell__spell_name'
    ).annotate(count=Count('id_spell__spell_name')
    ).order_by('-count')[:10]

# Jugadores que mayor cantidad de puntos de daño han ocasionado en todas las batallas efectuadas.
def Rank_damage_player():
    return models.Event.objects.values('id_attacker__character_name'
    ).annotate(damage_point=(Sum('health_points_before') - Sum('health_points_after'))
    ).order_by('-damage_point')[:10]

def used_spell():
    return models.KnownSpell.objects.filter(spell_used = True
    ).values('id_spell__spell_name'
    ).annotate(count=Count('id_spell__spell_name')
    ).order_by('count')[:10]
