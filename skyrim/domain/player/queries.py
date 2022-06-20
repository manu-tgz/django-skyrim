from skyrim.data.models import Player
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError


def get_player_list(user_id):
    """_summary_

    Args:
        user_id: The user who desires to obtain his players

    Returns:
        queryset: The User Players
    """
    try:
        players = Player.objects.filter(id_character__id_client = user_id)
    except ObjectDoesNotExist:
        print("Either the player doesn't exist.")  
    return players
    

def get_player(player_id):
    try:
        player =Player.objects.get(id=player_id)
    except ObjectDoesNotExist:
        print("Either the player doesn't exist.")  
        player = None   
    except OperationalError:
        print("no such table: data_playe.")
        player = None   
    return player