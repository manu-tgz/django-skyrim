from ..populate import Populate
from skyrim.domain.stats.statistics import  *
from django.test import TestCase
import datetime 

class StatsTestCase(TestCase):
    def setUp(self):
        Populate()
    
    def test_Beast_List(self):
        var = Beast_List()
        #Las bestias que estan en batallas
        result = [{'character__race_type__race_name': 'dragon', 'count': 1},
                  {'character__race_type__race_name': 'bird', 'count': 1}]
        self.assertEqual(var[0],result[0])
        self.assertEqual(var[1],result[1])
        print ("Beast_List..................................OK")
    
    def test_BattleDuration(self):
        var = BattleDuration()
        result = {'duration': {'id_battle': 1, 'count': 2}, 'info': {'place_id': 1, 'place_name': 'North',
         'date': datetime.date(2022, 2, 16), 'time': datetime.time(12, 30)}}
        self.assertEqual(var[0],result)
        print ("BattleDuration..............................OK")
    
    def test_Rank_n_attacks(self):
        var = Rank_n_attacks(5)
        result = {'id_attack': 1, 'id_attack__attack_type__type': 'fire', 'id_attack__damage_point': 10, 'count': 2}
        self.assertEqual(var[0],result)
        print ("Rank_n_attacks..............................OK")
    
    def test_know_spell(self):
        var = know_spell()
        result = [{'id_spell__spell_name': 'little avalanche', 'count': 5}, 
            {'id_spell__spell_name': 'little fireball', 'count': 3},
            {'id_spell__spell_name': 'little wave', 'count': 2}, 
            {'id_spell__spell_name': 'little air blast', 'count': 1}, 
            {'id_spell__spell_name': 'little spit', 'count': 1}, 
            {'id_spell__spell_name': 'medium air blast', 'count': 1},
            {'id_spell__spell_name': 'medium fireball', 'count': 1}]
        for v,r in zip(var,result):
            self.assertEqual(v,r)
        print ("know_spell..................................OK")
    
    def  test_Rank_damage_player(self):
        var = Rank_damage_player()
        result = [{'id_attacker__character_name': 'character1', 'damage_point': 20},
                {'id_attacker__character_name': 'character2', 'damage_point': 20}]
        for v,r in zip(var,result):
            self.assertEqual(v,r)
        print ("Rank_damage_player..........................OK")
    
    def test_used_spell(self):
        var = used_spell()
        result = [{'id_spell__spell_name': 'little avalanche', 'count': 1}, 
            {'id_spell__spell_name': 'little fireball', 'count': 1},
            {'id_spell__spell_name': 'little spit', 'count': 1}, 
            {'id_spell__spell_name': 'medium air blast', 'count': 1}]
        
        for v,r in zip(var,result):
            self.assertEqual(v,r)
        print ("used_spell..................................OK")
  