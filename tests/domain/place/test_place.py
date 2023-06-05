from ..populate import Populate
from skyrim.domain.place.queries import  *
from django.test import TestCase


class PlaceTestCase(TestCase):
    def setUp(self):
        Populate()
    def test_get_all_places(self):
        var =  get_all_places()
        result = [{'id': 1, 'name': 'North', 'type_id': 1, 'type_name': 'winter'}, 
                {'id': 2, 'name': 'Sahara', 'type_id': 2, 'type_name': 'desert'}, 
                {'id': 3, 'name': 'Andes', 'type_id': 3, 'type_name': 'Montain'}, 
                {'id': 4, 'name': 'Egipto', 'type_id': 4, 'type_name': 'beach'}]
        for v,r in zip(var,result):
                self.assertEqual(v,r)
        print ("get_all_places..............................OK")
    
        