from skyrim.data.models import Player, Beast
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError

def PlayerListQuery(user_id):
    # TODO: Convertir query a lista.
    try:
        players = Player.objects.filter(id_character__id_client = user_id)
    except ObjectDoesNotExist:
        print("Either the player doesn't exist.")  
        
    return players
    

def PlayerQuery(player_id):
    try:
        player =Player.objects.get(id=player_id)
    except ObjectDoesNotExist:
        print("Either the player doesn't exist.")  
        player = None   
    except OperationalError:
        print("no such table: data_playe.")
        player = None   
    return player


def BeastListQuery(user_id):
    # TODO: Convertir query a lista.
    try:
        beasts = Beast.objects.filter(id_character__id_client = user_id)
    except ObjectDoesNotExist:
        print("Either the beast doesn't exist.")       
    return beasts


def BeastQuery(beast_id):
    try:
        beast =Beast.objects.get(id=beast_id)
    except ObjectDoesNotExist:
        print("Either the beast doesn't exist.")  
        beast = None   
    except OperationalError:
        print("no such table: data_playe.")
        beast = None   
    return beast    