from skyrim.data.models import Character
from skyrim.domain.race.queries import get_weakness_from_character
from skyrim.domain.attack.queries import get_attack_from_character

class Character_for_Battle:
    name = None
    id_character = None
    ataques = None
    weakness_id = None
    hp = None
    def __init__(self,id_character = None, character_obj = None):
        character = None
        if(character_obj == None):
            if(not(id_character == None)):
                self.id_character = id_character
                character = Character.objects.get(id = id_character)
            else:
                raise Exception("Needs an id_character or character_obj parameter")
        else :
            self.id_character = character_obj.id
            character = character_obj
        self.name = character.character_name
        self.weakness_id = get_weakness_from_character(character)
        self.ataques = get_attack_from_character(character)
        self.hp = character.health_points
