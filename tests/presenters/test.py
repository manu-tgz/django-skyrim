from tests.presenters.abstract import (GetViewTest, LoginRequired, PostViewTest, 
                                       LOGIN_REDIRECT, GetViewTestLoginRequired, 
                                       PostViewTestLoginRequired)
from django.test import TestCase, RequestFactory
from skyrim.presenters.views import (index,register,create_beast_view,create_battle_view,
                                     query1, query2, query3, query4, query5, query6,
                                     user_profile,user_characters,tables,login,
                                     battle_details_view)
from skyrim.data.models import *
import datetime
from django.contrib.auth.views import LoginView, logout_then_login

class IndexTest(GetViewTestLoginRequired,TestCase):
    """IndexTest"""
    function = index
    url = '/index'
    template = 'index.html'
    redirect = LOGIN_REDIRECT + url


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
        
#     # def test_password_incorrect(self):
#     #         response = self.client.post(self.url, data={"username":"manu",
#     #                                                 "email": "example@gmail.com",
#     #                                                 "password": "test**1234",
#     #                                                 "password2":"test**123"})

class CreateBeastTest(PostViewTestLoginRequired, TestCase):
    """CreateBeastTest"""

    function = create_beast_view
    url = '/create_beast/'
    template = 'create_beast.html'
    redirect = LOGIN_REDIRECT+url
       
    def get_data(self):
        data= {"pedro": [1,2],
               "name": "Luisa",
               "race": 1,
               "health_points": 12,
               "blow":1
        }

class CreateBattleTest(PostViewTestLoginRequired, TestCase):
    """CreateBattleTest"""
    
    function = create_battle_view
    url = '/create_battle/'
    template = 'select_character.html'
    redirect = LOGIN_REDIRECT+url
      
    def get_data(self):
        data= {"place": 1
        }

class BatleDetailsTest(GetViewTestLoginRequired,TestCase):
    """BatleDetailsTest"""
    
    function = battle_details_view
    url = '/battle_details'
    template = 'battle_details.html'
    redirect = LOGIN_REDIRECT + url
    
    def setUp(self):
        super().setUp()
        place_type1 = PlaceType.objects.create(type = 'winter')
        place1 = Place.objects.create(place_name = 'North',place_type= place_type1)
        battle1 = Battle.objects.create(place = place1, 
                                            date = datetime.date(2022,2,16),
                                            time = datetime.time(12,30))
    
    def get_url(self):
        return self.url+"/1/"

class Query1Test(GetViewTestLoginRequired, TestCase):
    """Query1Test"""
    
    function = query1
    url = '/query1/'
    template = 'query1.html'
    redirect = LOGIN_REDIRECT + url
    

class Query2Test(GetViewTestLoginRequired, TestCase):
    """Query2Test"""
    
    function = query2
    url = '/query2/'
    template = 'query2.html'
    redirect = LOGIN_REDIRECT + url
       
class Query3Test(GetViewTestLoginRequired, TestCase):
    """Query3Test"""
    
    function = query3
    url = '/query3/'
    template = 'query3.html'
    redirect = LOGIN_REDIRECT + url

class Query4Test(GetViewTestLoginRequired, TestCase):
    """Query4Test"""
    
    function = query4
    url = '/query4/'
    template = 'query4.html'
    redirect = LOGIN_REDIRECT + url    

class Query5Test(GetViewTestLoginRequired, TestCase):
    """Query5Test"""
    
    function = query5
    url = '/query5/'
    template = 'query5.html'
    redirect = LOGIN_REDIRECT + url 
    
class Query6Test(GetViewTestLoginRequired, TestCase):
    """Query6Test"""
    
    function = query6
    url = '/query6/'
    template = 'query6.html'
    redirect = LOGIN_REDIRECT + url 
    
class UserProfileTest(PostViewTestLoginRequired,TestCase):
    """UserProfileTest"""

    function = user_profile
    url = '/user_profile/'
    template = 'user_profile.html'
    redirect = LOGIN_REDIRECT + url 
    
    def get_data(self):
        data={"username1":"manu1","email": "example1@gmail.com",
              "first_name":"lo", "last_name":"Tu",
              "password1": "test**1234","password2":"test**1234"}
        return data

# class UserCharactersTest(GetViewTestLoginRequired,TestCase):
#     """CreatePlayerTest"""
#     function = user_characters
#     url = '/user_characters/'
#     template = 'user_characters.html'
    
#     def get_url(self):
#         return self.url+"1/"

class TablesTest(GetViewTestLoginRequired, TestCase):
    """TablesTest"""
    
    function = tables
    url = '/tables'
    template = 'tables.html'
    redirect = LOGIN_REDIRECT + url
    
class LoginTest(GetViewTest, TestCase):
    """LoginTest"""
    
    function = LoginView.as_view()
    url = '/login/' 
    template = 'login.html'



