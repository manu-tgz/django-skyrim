from ..populate import Populate
from skyrim.domain.battle.queries import  *
from django.test import TestCase


class BattleTestCase(TestCase):       
    def setUp(self):
        Populate()
    
    def test_get_battle(self):
        battle = get_battle(1)
        battle_result =  Battle.objects.first()
        result = {
        'place_id': battle_result.place.id,
        'place_name' : battle_result.place.place_name,
        'date' : battle_result.date,
        'time': battle_result.time}
        self.assertEqual(result, battle)
        print ("get_battle..................................OK")


    def test_get_characters_from_battle(self):
        characters = get_characters_from_battle(1)
        result = []
        result.append({
            'id':1,
            'Nombre':'character1',
            'Raza_label':'dragon',
            'Raza_key':6,
            'Puntos_de_Vida':500,
            'Creador_label':'user1',
            'Creador_key':1,
        })
        
        result.append({
            'id':2,
            'Nombre':'character2',
            'Raza_label':'bird',
            'Raza_key':10,
            'Puntos_de_Vida':700,
            'Creador_label':'user1',
            'Creador_key':1,
        })

        self.assertEqual(result,characters)
        print ("get_characters_from_battle..................OK")


    def test_get_characters_obj_from_battle(self):
        characters = get_characters_obj_from_battle(1)
        
        self.assertEqual(characters[0].hp,500)
        self.assertEqual(characters[0].id_character,1)
        self.assertEqual(characters[0].name,'character1')
        self.assertEqual(characters[0].weakness_id,1)
    
        self.assertEqual(characters[1].hp,700)
        self.assertEqual(characters[1].id_character,2)
        self.assertEqual(characters[1].name,'character2')
        self.assertEqual(characters[1].weakness_id,2)
        print ("get_characters_obj_from_battle..............OK")
    
    def test_get_winner(self):
        winner = get_winner(2)
        result = {}
        result['winner_id'] = 2
        result['name'] = 'character2'
        result['battle_id'] = 2
        self.assertEqual(winner,result)
        print ("get_winner..................................OK")

    def test_get_battle_stats(self):
        var = get_battle_stats(1)
        
        result = {  
        'most_violent': [{'id_attacker__character_name': 'character1', 'damage_points': 20}, 
        {'id_attacker__character_name': 'character2', 'damage_points': 20}],
         
        'less_violent':[{'id_attacker__character_name': 'character1', 'damage_points': 20},
        {'id_attacker__character_name': 'character2', 'damage_points': 20}],
        
        'most_damaged': [{'id_damaged__character_name': 'character2', 'damage_points': 20}, 
        {'id_damaged__character_name': 'character3', 'damage_points': 20}], 
        
        'less_damaged':[{'id_damaged__character_name': 'character2', 'damage_points': 20}, 
        {'id_damaged__character_name': 'character3', 'damage_points': 20}]
        }
        
        for value_var in var:
            var0 = var[value_var]
            result0 = result[value_var]
            for v,r in zip(var0,result0):
                self.assertEqual(v,r)
        print ("get_battle_stats...........................OK")
      