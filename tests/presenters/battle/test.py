from django.test import TestCase
from tests.presenters.abstract import GetViewTest
from skyrim.presenters.battle.generar_batalla_aleatoria_view import generar_batalla_aleatoria_view
from skyrim.data.models import *

class GenerateRandomBattleTest(GetViewTest,TestCase):
    """CreatePlayerTest"""
    function = generar_batalla_aleatoria_view
    url = '/generar_batalla_aleatoria/'
    # template = 'create_player.html'
    status_code = None
    
    def setUp(self):
        user = User(email= 'example@gmail.com', username='user1', password='123')
        user.save()
        fire = DamageType(type = 'fire')
        fire.save()
        stone = DamageType(type = 'stone')
        stone.save()
        water = DamageType(type = 'water')
        water.save()
        
        paladin = Race(race_name = 'paladin',weakness = fire)
        paladin.save()
        warrior = Race(race_name = 'warrior',weakness = stone)
        warrior.save()
        mage = Race(race_name = 'mage',weakness = water)
        mage.save()
        
        character1 = Character(character_name = 'character1',
                                              race_type = paladin,health_points = 500,
                                              id_client= user)
        character1.save()
        character2 = Character(character_name = 'character2',
                                              race_type = warrior,health_points = 700,
                                              id_client= user)
        character2.save()
        character3 = Character(character_name = 'character3',
                                              race_type = mage,health_points = 400,
                                              id_client= user)
        character3.save()

    def get_response(self):
        response = self.client.get(self.url + "1/")
        return response
    
    def get_data(self):
        data = {'contestant': [1,2,3]}
        return data