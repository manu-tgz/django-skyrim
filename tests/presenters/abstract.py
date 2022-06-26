from re import template
from django.http import response
from django.urls import resolve
from django.test import TestCase, Client

class ViewTest():
    url =None
    function = None
    template = None
    
    def setUp(self):
        # need a browser customer 
        self.client = Client()
    
    def test_root_url(self):
        found = resolve(self.url)
        self.assertEqual(found.func.__name__, self.function.__name__)
        
    # def test_uses_template(self):
    #     response = self.get_response()
    #     self.assertTemplateUsed(response,template)
        
    def get_response(self):
        pass   
     
    class Meta:
        abstract = True