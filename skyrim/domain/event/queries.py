from skyrim.data.models import Event
from .classes import Event_for_Battle

def get_event_list(battle_id):
    event_list = Event.objects.filter(id_battle = battle_id)
    result = []
    for event in event_list:
        result.append(
            Event_for_Battle(
                id_event = event.id_event,
                id_battle = event.id_battle.id,
                id_attacker = event.id_attcker.id,
                id_damaged = event.id_damaged.id,
                id_attack = event.id_attack.id,
                health_points_before = event.health_points_before,
                health_points_after = event.health_points_after
            )
        )
    return result
