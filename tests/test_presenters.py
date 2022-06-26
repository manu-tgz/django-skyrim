from django import views
from django.test import TestCase, Client, RequestFactory
from skyrim.data.models import *
from skyrim.presenters.player.views import PlayerByUserView

class RegisterTest(TestCase):
    def setUp(self):
        # need a browser customer 
        self.client = Client()
    
    def test_register(self):
        response = self.client.post('/register/', {'username': 'fred',
                                        'email': 'secret',
                                        'password': 'password123',
                                        'password2': 'password123',})
        
        self.assertEqual(response.status_code, 200)
               
class ListPlayerTest(TestCase):
    def setUp(self):
        # need a browser customer 
        self.factory = RequestFactory()
        self.user = User.objects.create(username ='fred',email ='secret',
                                        password='top_secret')
    
    def test_player_by_user(self):
        request = self.factory.get('player_list')
        request.user = self.user
        response =  PlayerByUserView.as_view()(request)
        self.assertEqual(response.status_code, 200)
           
           
        