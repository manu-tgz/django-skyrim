from skyrim.data.models import Event, Battle, Character, Attack

def insert_several_events_same_battle(Events):
    #obteniendo la batalla una sola vez
    battle = Battle.objects.get(id = Events[0].id_battle)

    #obteniendo los characters una sola vez
    characters_id = []
    for event in Events:
        characters_id.append(event.id_attacker)
        characters_id.append(event.id_damaged)
    characters_id_unique = list(set(characters_id))

    characters_unique = []

    for id in characters_id_unique:
        character = Character.objects.get(id = id)
        characters_unique.append(character)

    #obteniendo los attack una sola vez

    attacks_id = [] 
    for event in Events:
        attacks_id.append(event.id_attack)
    attacks_id_unique = list(set(attacks_id))

    attacks_unique = []
    for id in attacks_id_unique:
        attack = Attack.objects.get(id = id)
        attacks_unique.append(attack)

    #añadiendo los eventos

    for event in Events:
        #tomar ataque
        attack_index = attacks_id_unique.index(event.id_attack)
        #tomar atacante 
        attacker_index = characters_id_unique.index(event.id_attacker)
        #tomar atacado
        damaged_index = characters_id_unique.index(event.id_damaged)
        #insertar evento
        e = Event(
            id_event = event.id_event,
            id_battle = battle,
            id_attacker = characters_unique[attacker_index],
            id_damaged = characters_unique[damaged_index],
            id_attack = attacks_unique[attack_index],
            health_points_before = event.health_points_before, 
            health_points_after = event.health_points_after)
        e.save()
    

