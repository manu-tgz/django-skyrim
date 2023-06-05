
class Attack_for_Battle:
    id = None
    attack_type = None
    damage = None
    def __init__(self, attack):
        self.id = attack.id
        self.damage = attack.damage_point
        self.attack_type = attack.attack_type.id
