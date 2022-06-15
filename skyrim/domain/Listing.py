from skyrim.data.models import Player, Beast

def PlayerListQuery(user_id):
    # TODO: Convertir query a lista.  
    return Player.objects.filter(id_character__id_client = user_id)
    

def PlayerQuery(player_id):
    return Player.objects.get(id=player_id)


def BeastListQuery(user_id):
    # TODO: Convertir query a lista.  
    return None#Beast.objects.filter(id_character__id_client = user_id)


def BeastQuery(beast_id):
    return None #Beast.objects.get(id=beast_id)