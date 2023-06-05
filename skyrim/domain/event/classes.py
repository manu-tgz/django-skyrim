

class Event_for_Battle:
    id_event = None,
    id_battle = None,
    id_attacker = None,
    id_damaged = None,
    id_attack = None,
    health_points_before = None, 
    health_points_after = None,
    
    def __init__(self,id_event,id_battle,id_attacker,id_damaged,id_attack,health_points_before,health_points_after):
        self.id_event = id_event
        self.id_battle = id_battle
        self. id_attacker = id_attacker
        self.id_damaged = id_damaged
        self.id_attack = id_attack
        self.health_points_before = health_points_before
        self.health_points_after =  health_points_after