from ..populate import Populate
from skyrim.domain.event.queries import  *
from django.test import TestCase
from skyrim.data.models import *

        
class EventTestCase(TestCase):
    def setUp(self):
        Populate()
    def test_get_event_list(self):
        var = get_event_list(Battle.objects.first())
        result = []
        result.append(Event_for_Battle(
                id_event = 1,
                id_battle = 1,
                id_attacker = 1,
                id_damaged = 2,
                id_attack = 1,
                health_points_before = 100,
                health_points_after = 80))
        result.append(Event_for_Battle(
                id_event = 2,
                id_battle = 1,
                id_attacker = 2,
                id_damaged = 3,
                id_attack = 1,
                health_points_before = 100,
                health_points_after = 80))

        for v,r in zip(var,result):
            self.assertEqual(v.id_event,r.id_event)
            self.assertEqual(v.id_battle,r.id_battle)
            self.assertEqual(v.id_attacker,r.id_attacker)
            self.assertEqual(v.id_damaged,r.id_damaged)
            self.assertEqual(v.id_attack,r.id_attack)
            self.assertEqual(v.health_points_before,r.health_points_before)
            self.assertEqual(v.health_points_after ,r.health_points_after )
        print ("get_event_list..............................OK")
        