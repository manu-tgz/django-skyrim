from http.client import ImproperConnectionState
import imp
from skyrim.data.models import Character
from skyrim.domain.race.queries import get_weakness_from_character
from skyrim.domain.attack.queries import get_attack_from_character

class Character_for_Battle:
    id_character = None
    ataques = None
    weakness_id = None
    hp = None
    def __init__(self,id_character):
        self.id_character = id_character
        character = Character.objects.get(id = id_character)
        self.weakness_id = get_weakness_from_character(character)
        self.ataques = get_attack_from_character(character)
        self.hp = character.health_points
