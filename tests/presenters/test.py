from tests.presenters.abstract import ViewTest
from django.test import TestCase, RequestFactory
from skyrim.presenters.views import (index,register,create_beast_view,
                                     create_battle_view)


class IndexTest(ViewTest,TestCase):
    print("----------------IndexTest -----------------")

    function = index
    url = '/'
    template = 'index.html'
    
    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
        return super().setUp()
    
    def get_response(self):
        response = self.client.get(self.url)
        return response

class RegisterTest(ViewTest,TestCase):
    print("----------------RegisterTest -----------------")

    function = register
    url = '/register'
    template = 'register.html'
    
    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
        return super().setUp()
    
    def get_response(self):
        response = self.client.post(self.url)
        return response
        
    # def test_password_incorrect(self):
    #         response = self.client.post(self.url, data={"username":"manu",
    #                                                 "email": "example@gmail.com",
    #                                                 "password": "test**1234",
    #                                                 "password2":"test**1234"})

class CreateBeastTest(ViewTest,TestCase):
    print("-------------CreateBeastTest --------------")

    function = create_beast_view
    url = '/create_beast/'
    template = 'create_beast.html'
    
    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
        return super().setUp()
    
    def get_response(self):
        response = self.client.post(self.url)
        return response


class CreateBattleTest(ViewTest,TestCase):
    print("---------------CreateTest-----------------")

    function = create_battle_view
    url = '/create_battle/'
    template = 'select_character.html'
    
    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
        return super().setUp()
    
    def get_response(self):
        response = self.client.post(self.url)
        return response