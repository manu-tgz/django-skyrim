from multiprocessing import context
from django.urls import resolve
from django.test import TestCase, Client
from skyrim.data.models import User

LOGIN_REDIRECT = "/accounts/login/?next="

class ViewTest():
    url =None
    function = None
    template = None
    status_code = 200
    redirect= None
    
    def setUp(self):
        # need a browser customer 
        self.client = Client()
    def get_url(self):
        """Return url for test_root_url and test_return_correct_out
        Those are base case by test
        """
        return self.url
      
    def get_data(self):
        """Generate a correct data
        """
        pass
        
    def test_root_url(self):
        """Check the view is the correct"""
        found = resolve(self.get_url())
        print("function name: {} {}----------".format(found.func.__name__, self.function.__name__))
        self.assertEqual(found.func.__name__, self.function.__name__)
        
    def test_return_correct_out(self):
        """Test response from client.get() or client.post
        - Test status code
        - Test out file is correct or redirect link if have redirect
        - Test context data
        """
        response = self.get_response()
        self.assertEqual(response.status_code,self.status_code)
        self.check_out(response)
        self.check_context_data(response)
      
    def uses_redirect(self, response):
        self.assertEqual(response['location'], self.redirect)
    
    def check_out(self, response):
        if self.redirect is None:
            return self.check_html(response)  
        else:
            self.uses_redirect(response)   
    
    def check_context_data(self, response):
        pass
          
    def check_html(self, response):
        # TODO: Cuando integren los html
        # self.is_working(response)
        self.uses_template(response)
                      
    def uses_template(self, response):
        """Checking what templated are used"""
        prueba = response
        self.assertTemplateUsed(response,self.template)          
        
    
    def is_working(self, response):
        """Just to make sure everything is working"""
        html = response.content.decode('utf8')
        self.assertIn("Colocar html aqui", html)
        
    def get_response(self):
        pass   
     
    class Meta:
        abstract = True
        
class PostViewTest(ViewTest):
    
    def get_response(self):
        response = self.client.post(self.get_url(), data=self.get_data())
        return response
                   
class GetViewTest(ViewTest):

    def get_response(self):
        response = self.client.get(self.get_url(), data=self.get_data())
        return response

class LoginRequired():
    def login(self, client):
       user,created = User.objects.get_or_create(email= 'example@gmail.com', username='user1', password='ppfn32123')
       client.login(username= user.username, password= user.password) 
    
class PostViewTestLoginRequired(LoginRequired, PostViewTest):
    status_code = 302
    def setUp(self):
        super().setUp()
        self.login(self.client)
        
class GetViewTestLoginRequired(LoginRequired, GetViewTest):    
    status_code = 302
    def setUp(self):
        super().setUp()
        self.login(self.client)    
    
    
    