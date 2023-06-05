from ..populate import Populate
from skyrim.domain.beast.queries import  *
from django.test import TestCase

class BeastTestCase(TestCase):
    def setUp(self):
        Populate()

    def test_get_beast(self):
        beast = get_beast(1)
        try:
            self.assertEqual(beast.id, 1)
            print ("get_beast...................................OK")
        except:
            self.assertEqual(beast.id, 1)
            print ("get_beast...................................F")

    def test_get_beast_list(self):
        beasts = get_beast_list(1)
        result =Beast.objects.all()
        self.assertEqual(str(beasts), str(result))
        print ("get_beast_list..............................OK")
        