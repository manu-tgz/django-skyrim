from django.test import TestCase, RequestFactory
from skyrim.data.models import *
from skyrim.presenters.player.views import  PlayerView
from tests.presenters.abstract import ViewTest, GetViewTest, PostViewTest
from skyrim.presenters.views import create_player_view

# class ListPlayerTest():
#     def setUp(self):
#         # need a browser customer
#         self.factory = RequestFactory()
#         self.user = User.objects.create(username ='fred',email ='secret',
#                                         password='top_secret')

class CreatePlayerTest(PostViewTest,TestCase):
    """CreatePlayerTest"""
    function = create_player_view
    url = '/create_player/'
    template = 'create_player.html'
    status_code = 302
    redirect = "/accounts/login/?next="+url

    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
       super().setUp()
       user,created = User.objects.get_or_create(email= '', username='user1', password='ppfn32123')
       self.client.login(username='user1', password='ppfn32123')
       
    def get_data(self):
        data= {"name":"Robert",
               "race_id": 1,
               "health_points":12,
               "pedro": [1,2]
        }


class GetPlayerTest(GetViewTest,TestCase):
    """CreatePlayerTest"""
    function = PlayerView.as_view()
    url = '/player/'
    template = 'test copy.html'
    

    def setUp(self):
       super().setUp()
       fire = DamageType.objects.create(type = 'fire')
       fire.save()
       paladin = Race.objects.create(race_name = 'paladin',weakness = fire)
       paladin.save()
       player_race = PlayerRace.objects.create(id_race=paladin)
       player_race.save()
       user, created = User.objects.get_or_create(email= 'example@gmail.com', username='user1', password='ppfn32123')
       user.save()
       character1 = Character.objects.create(character_name = 'character1',race_type = paladin,health_points = 500,id_client= user)
       character1.save()
       player1 = Player(id_character = character1)
       player1.save()
       arkigj = player1
    
    def get_url(self):
        return self.url+"1/"

    def check_context_data(self, response):
        return super().check_context_data(response)
