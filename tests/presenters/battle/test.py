from django.test import TestCase
from tests.presenters.abstract import GetViewTest
from skyrim.presenters.battle.generar_batalla_aleatoria_view import generar_batalla_aleatoria_view
from skyrim.data.models import *


class GenerateRandomBattleTest(GetViewTest,TestCase):
    """CreatePlayerTest"""
    function = generar_batalla_aleatoria_view
    url = '/create_player/'
    template = 'create_player.html'
    def setUp(self):
        user = User(email= '', username='user1', password='123')
        
        fire = DamageType.objects.create(type = 'fire')
        stone = DamageType.objects.create(type = 'stone')
        water = DamageType.objects.create(type = 'water')
        
        paladin = Race.objects.create(race_name = 'paladin',weakness = fire)
        warrior = Race.objects.create(race_name = 'warrior',weakness = stone)
        mage = Race.objects.create(race_name = 'mage',weakness = water)
        
        character1 = Character.objects.create(character_name = 'character1',
                                              race_type = paladin,health_points = 500,
                                              id_client= user)
        character2 = Character.objects.create(character_name = 'character2',
                                              race_type = warrior,health_points = 700,
                                              id_client= user)
        character3 = Character.objects.create(character_name = 'character3',
                                              race_type = mage,health_points = 400,
                                              id_client= user)

    def get_response(self):
        response = self.client.get(self.url + "1/")
        return response
    
    def get_data(self):
        data = {'contestant': [1,2,3]}