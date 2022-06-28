from ..populate import Populate
from skyrim.domain.attack.queries import  *
from skyrim.domain.attack.classes import Attack_for_Battle
from django.test import TestCase
from skyrim.domain.spell.queries import * 

class AttackTestCase(TestCase):
    def setUp(self):
        Populate()

    def compareAttacks(self,querie, result):
        for q,r in zip(querie,result):
            self.assertEqual(q.id,r.id)
            self.assertEqual(q.attack_type,r.attack_type)
            self.assertEqual(q.damage,r.damage)

    def test_get_attack_from_character_id(self):
        '''El tester testea sobre la quierie `test_get_attack_from_character_id` pero con el se aseguran los queries de :
          `get_attack_from_character_id`, 
          `get_attack_from_character`, 
          `get_attack_from_player`, 
          `get_attack_from_player_id`, 
          `get_attack_from_beast`, 
          `get_attack_from_beast_id`.'''

        id_character = 1
        blow = get_attack_from_character_id(id_character)
        blow_result =[Attack_for_Battle(Blow.objects.first().id_blow)]
        self.compareAttacks(blow,blow_result)
    
        id_character = 2
        blow1 = get_attack_from_character_id(id_character)
        blow_result1 =[Attack_for_Battle(Blow.objects.get(id_blow = 22).id_blow)]
        self.compareAttacks(blow1,blow_result1)

        id_character = 6
        spell = get_attack_from_character_id(id_character);
        spell_result = []
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 1).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 2).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 3).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 4).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 5).id_spell))
        self.compareAttacks(spell, spell_result)

        id_character = 8
        spell = get_attack_from_character_id(id_character);
        spell_result.clear()
        spell_result= []
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 3).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 1).id_spell))
        self.compareAttacks(spell, spell_result)


        id_character = 9
        spell =get_attack_from_character_id(id_character);
        spell_result.clear()
        spell_result= []
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 3).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 7).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 4).id_spell))
        self.compareAttacks(spell, spell_result)
        
        id_character = 10
        spell =get_attack_from_character_id(id_character);
        spell_result.clear()
        spell_result= []
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 3).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 1).id_spell))
        spell_result.append(Attack_for_Battle(Spell.objects.get(id_spell = 6).id_spell))
        self.compareAttacks(spell, spell_result)
        print ("get_attack_from_character...................OK")
        print ("get_attack_from_character_id................OK")
        print ("get_attack_from_player......................OK")
        print ("get_attack_from_player_id...................OK")
        print ("get_attack_from_beast.......................OK")
        print ("get_attack_from_beast_id....................OK")

    def test_get_all_blows(self):
        blows = get_all_blows()
        self.assertEqual(blows[0] ,{'id': 21, 'damage': 11, 'attack_type_id': 1, 'attack_type_name': 'fire'}    )
        self.assertEqual(blows[1] ,{'id': 22, 'damage': 11, 'attack_type_id': 2, 'attack_type_name': 'air'})
        self.assertEqual(blows[2] ,{'id': 23, 'damage': 11, 'attack_type_id': 3, 'attack_type_name': 'stone'})
        self.assertEqual(blows[3] ,{'id': 24, 'damage': 11, 'attack_type_id': 4, 'attack_type_name': 'water'})
        self.assertEqual(blows[4] ,{'id': 25, 'damage': 11, 'attack_type_id': 5, 'attack_type_name': 'poison'})
        self.assertEqual(blows[5] ,{'id': 26, 'damage': 16, 'attack_type_id': 1, 'attack_type_name': 'fire'})
        self.assertEqual(blows[6] ,{'id': 27, 'damage': 16, 'attack_type_id': 2, 'attack_type_name': 'air'})
        self.assertEqual(blows[7] ,{'id': 28, 'damage': 16, 'attack_type_id': 3, 'attack_type_name': 'stone'})
        self.assertEqual(blows[8] ,{'id': 29, 'damage': 16, 'attack_type_id': 4, 'attack_type_name': 'water'})
        self.assertEqual(blows[9] ,{'id': 30, 'damage': 16, 'attack_type_id': 5, 'attack_type_name': 'poison'})
        self.assertEqual(blows[10] ,{'id': 31, 'damage': 21, 'attack_type_id': 1, 'attack_type_name': 'fire'})
        self.assertEqual(blows[11] ,{'id': 32, 'damage': 21, 'attack_type_id': 2, 'attack_type_name': 'air'})
        self.assertEqual(blows[12] ,{'id': 33, 'damage': 21, 'attack_type_id': 3, 'attack_type_name': 'stone'})
        self.assertEqual(blows[13] ,{'id': 34, 'damage': 21, 'attack_type_id': 4, 'attack_type_name': 'water'})
        self.assertEqual(blows[14] ,{'id': 35, 'damage': 21, 'attack_type_id': 5, 'attack_type_name': 'poison'})
        self.assertEqual(blows[15] ,{'id': 36, 'damage': 26, 'attack_type_id': 1, 'attack_type_name': 'fire'})
        self.assertEqual(blows[16] ,{'id': 37, 'damage': 26, 'attack_type_id': 2, 'attack_type_name': 'air'})
        self.assertEqual(blows[17] ,{'id': 38, 'damage': 26, 'attack_type_id': 3, 'attack_type_name': 'stone'})
        self.assertEqual(blows[18] ,{'id': 39, 'damage': 26, 'attack_type_id': 4, 'attack_type_name': 'water'})
        self.assertEqual(blows[19] ,{'id': 40, 'damage': 26, 'attack_type_id': 5, 'attack_type_name': 'poison'})
        self.assertEqual(len(blows), 20)
        print ("get_all_blows...............................OK")
