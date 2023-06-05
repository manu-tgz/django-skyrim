from ..populate import Populate
from skyrim.domain.character.queries import  *
from django.test import TestCase

class CharacterTestCase(TestCase):
    def setUp(self):
        Populate()

    def test_get_character_union_filters_by_user(self):
        var = get_character_union_filters_by_user(1)
        result = []
        result.append({'id': 1, 'Nombre': 'character1', 'Raza_label': 'dragon', 'Raza_key': 6, 'Puntos_de_Vida': 500, 'Tipo': 'player'})
        result.append({'id': 2, 'Nombre': 'character2', 'Raza_label': 'bird', 'Raza_key': 10, 'Puntos_de_Vida': 700, 'Tipo': 'player'})
        result.append({'id': 3, 'Nombre': 'character3', 'Raza_label': 'naga', 'Raza_key': 9, 'Puntos_de_Vida': 400, 'Tipo': 'player'})
        result.append({'id': 4, 'Nombre': 'character4', 'Raza_label': 'tiny', 'Raza_key': 8, 'Puntos_de_Vida': 550, 'Tipo': 'player'})
        result.append({'id': 5, 'Nombre': 'character5', 'Raza_label': 'zombie', 'Raza_key': 7, 'Puntos_de_Vida': 570, 'Tipo': 'player'})
        result.append({'id': 6, 'Nombre': 'character6', 'Raza_label': 'paladin', 'Raza_key': 1, 'Puntos_de_Vida': 500, 'Tipo': 'beast'})
        result.append({'id': 7, 'Nombre': 'character7', 'Raza_label': 'warrior', 'Raza_key': 3, 'Puntos_de_Vida': 700, 'Tipo': 'beast'})
        result.append({'id': 8, 'Nombre': 'character8', 'Raza_label': 'mage', 'Raza_key': 4, 'Puntos_de_Vida': 400, 'Tipo': 'beast'})
        result.append({'id': 9, 'Nombre': 'character9', 'Raza_label': 'nigromant', 'Raza_key': 5, 'Puntos_de_Vida': 550, 'Tipo': 'beast'})
        result.append({'id': 10, 'Nombre': 'character10', 'Raza_label': 'archer', 'Raza_key': 2, 'Puntos_de_Vida': 570, 'Tipo': 'beast'})
        self.assertEqual(var, result)
        print ("get_character_union_filters_by_user.........OK")
