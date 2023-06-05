from django.test import TestCase
from tests.presenters.abstract import (PostViewTestLoginRequired, GetViewTest, PostViewTest,
                                       LOGIN_REDIRECT, GetViewTestLoginRequired)
from skyrim.data.models import *
from skyrim.presenters.character.views import select_character_view
import datetime


class SelectCharacter(GetViewTest, TestCase):
    """SelectCharacter"""
    function = select_character_view
    url = '/'
    template = 'select_character.html' 

    def setUp(self):
        super().setUp()
        place_type1 = PlaceType.objects.create(type = 'winter')
        place1 = Place.objects.create(place_name = 'North',place_type= place_type1)
        battle1 = Battle.objects.create(place = place1, 
                                            date = datetime.date(2022,2,16),
                                            time = datetime.time(12,30))
    
    def get_url(self):
        return self.url +"1/"