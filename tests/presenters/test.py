from django.shortcuts import redirect
from tests.presenters.abstract import ViewTest,GetViewTest,PostViewTest
from django.test import TestCase, RequestFactory
from skyrim.presenters.views import (index,register,create_beast_view,
                                     create_battle_view)
from skyrim.data.models import *



class IndexTest(GetViewTest,TestCase):
    """IndexTest"""
    function = index
    url = '/index'
    template = 'index.html'
    
    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
       super().setUp()
       user,created = User.objects.get_or_create(email= 'example@gmail.com', username='user1', password='ppfn32123')
       self.client.login(username= user.username, password= user.password)
    


class RegisterTest(PostViewTest,TestCase):
    """RegisterTest"""

    function = register
    url = '/register'
    template = 'login.html'
    redirect = '/login/'
    status_code=302
    
    def get_data(self):
        data={"username1":"manu1","email": "example1@gmail.com",
              "first_name":"lo", "last_name":"Tu",
              "password1": "test**1234","password2":"test**1234"}
        return data
    
    def uses_template(self, response):
        response = self.get_response()
        # TODO: Cuando integren los html
        # self.is_working(response)
        self.uses_template(response)
        
    # def test_password_incorrect(self):
    #         response = self.client.post(self.url, data={"username":"manu",
    #                                                 "email": "example@gmail.com",
    #                                                 "password": "test**1234",
    #                                                 "password2":"test**123"})

# class CreateBeastTest(ViewTest,TestCase):
#     """CreateBeastTest"""

#     function = create_beast_view
#     url = '/create_beast/'
#     template = 'create_beast.html'
    
#     def setUp(self):
#         # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
#         return super().setUp()
    
#     def get_response(self):
#         response = self.client.post(self.url)
#         return response


class CreateBattleTest(ViewTest,TestCase):
    """CreateBattleTest"""
    
    function = create_battle_view
    url = '/create_battle/'
    template = 'create_battle.html'
    
    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
       super().setUp()
       user,created = User.objects.get_or_create(email= 'example@gmail.com', username='user1', password='ppfn32123')
       self.client.login(username= user.username, password= user.password)
    
    def get_response(self):
        response = self.client.get(self.url)
        return response