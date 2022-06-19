from skyrim.data.models import Beast
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError


def get_beast_list(user_id):
    try:
        beasts = Beast.objects.filter(id_character__id_client = user_id)
    except ObjectDoesNotExist:
        print("Either the beast doesn't exist.")       
    return beasts


def get_beast(beast_id):
    try:
        beast =Beast.objects.get(id=beast_id)
    except ObjectDoesNotExist:
        print("Either the beast doesn't exist.")  
        beast = None   
    except OperationalError:
        print("no such table: data_playe.")
        beast = None   
    return beast    