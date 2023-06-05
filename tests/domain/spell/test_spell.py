from ..populate import Populate
from skyrim.domain.spell.queries import  *
from django.test import TestCase


class SpellTestCase(TestCase):
    def setUp(self):
        Populate()
    
    def test_get_all_spells(self):
        var = get_all_spells()
        result = [
            {'spell_name': 'little fireball', 'id_spell_id': 1},
            {'spell_name': 'little air blast', 'id_spell_id': 2},
            {'spell_name': 'little avalanche', 'id_spell_id': 3},
            {'spell_name': 'little wave', 'id_spell_id': 4},
            {'spell_name': 'little spit', 'id_spell_id': 5}, 
            {'spell_name': 'medium fireball', 'id_spell_id': 6}, 
            {'spell_name': 'medium air blast', 'id_spell_id': 7}, 
            {'spell_name': 'medium avalanche', 'id_spell_id': 8},
            {'spell_name': 'medium wave', 'id_spell_id': 9}, 
            {'spell_name': 'medium spit', 'id_spell_id': 10}, 
            {'spell_name': 'big fireball', 'id_spell_id': 11},
            {'spell_name': 'big air blast', 'id_spell_id': 12}, 
            {'spell_name': 'big avalanche', 'id_spell_id': 13}, 
            {'spell_name': 'big wave', 'id_spell_id': 14}, 
            {'spell_name': 'big spit', 'id_spell_id': 15}, 
            {'spell_name': 'colossal fireball', 'id_spell_id': 16}, 
            {'spell_name': 'colossal air blast', 'id_spell_id': 17},
            {'spell_name': 'colossal avalanche', 'id_spell_id': 18},
            {'spell_name': 'colossal wave', 'id_spell_id': 19}, 
            {'spell_name': 'colossal spit', 'id_spell_id': 20}]
        for i in range(20):
            self.assertEqual(var[i],result[i])
        print ("get_all_spells..............................OK")
