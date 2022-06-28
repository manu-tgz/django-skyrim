from ..populate import Populate
from skyrim.domain.race.queries import  *
from django.test import TestCase
from skyrim.data.models import *

class RaceTestCase(TestCase):
    def setUp(self):
        Populate()
       
    def test_get_weakness_from_character_id(self):
        '''Tester para las queries `get_weakness_from_character_id` y `get_weakness_from_character`.'''
        weakness = get_weakness_from_character_id(1)
        result = DamageType.objects.first().id
        self.assertEqual(weakness,result)

        weakness = get_weakness_from_character_id(4)
        result = 3
        self.assertEqual(weakness,result)
        
        weakness = get_weakness_from_character_id(7)
        result = 3
        self.assertEqual(weakness,result)
        print ("get_weakness_from_character_id..............OK")
        print ("get_weakness_from_character.................OK")
    
    def test_get_all_player_races(self):    
        var = get_all_player_races()
        result = []
        result.append({'id': 1, 'name': 'paladin', 'weakness_id': 1})
        result.append({'id': 4, 'name': 'mage', 'weakness_id': 4})
        result.append({'id': 3, 'name': 'warrior', 'weakness_id': 3})
        result.append({'id': 5, 'name': 'nigromant', 'weakness_id': 5})
        result.append({'id': 2, 'name': 'archer', 'weakness_id': 2})
        self.assertEqual(var,result)
        print ("get_all_player_races........................OK")
