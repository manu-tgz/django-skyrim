from skyrim.data.models import Character, Player, Beast, Blow
from skyrim.domain.attack.classes import Attack_for_Battle


def get_attack_from_character_id(id_character):
    character = Character.objects.get(id = id_character)
    return get_attack_from_character(character)

def get_attack_from_character(character):
    if(hasattr(character,'player') ):
        value = character.player
        return get_attack_from_player(value)
    else:
        if(hasattr(character,'beast') ):
            value = character.beast
            return get_attack_from_beast(value)
        else:
            raise Exception(str(character.id) + ' no corresponde a ninguna bestia o jugador')


def get_attack_from_player_id(id_player):
    player = Player.objects.get(id = id_player)
    return get_attack_from_player(player)

def get_attack_from_player(player):
    known_spells = player.knownspell_set.all()
    result = []
    for spell in known_spells:
        result.append( Attack_for_Battle(spell.id_spell.id_spell))
    return result

def get_attack_from_beast_id(id_beast):
    beast = Beast.objects.get(id = id_beast)
    return get_attack_from_beast(beast)
    
def get_attack_from_beast(beast):
    attack_query = beast.id_attack.id_blow
    attack = Attack_for_Battle(attack_query)
    return [attack]

def get_all_blows():
    blow_list = Blow.objects.all()
    result = []
    for blow in blow_list:
        current = {}
        attack = blow.id_blow
        current["id"] = attack.id
        current["damage"] = attack.damage_point
        attack_type = attack.attack_type
        current["attack_type_id"] = attack_type.id
        current["attack_type_name"] = attack_type.type
        result.append(current)
    return result
