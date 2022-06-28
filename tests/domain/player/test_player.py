from ..populate import Populate
from skyrim.domain.player.queries import  *
from django.test import TestCase

class PlayerTestCase(TestCase):
    def setUp(self):
        Populate()
       
    def test_get_player_list(self):
        #no tiene problema usar los nombres de character xq son unicos
        players = get_player_list(1)
        self.assertEqual(str(players), str(Player.objects.all()))
        print ("get_player_list.............................OK")

    def test_get_player(self):
        player = get_player(1)
        self.assertEqual(player, Player.objects.first())
        print ("get_player..................................OK")
