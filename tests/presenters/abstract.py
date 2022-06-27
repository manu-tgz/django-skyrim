from django.urls import resolve
from django.test import TestCase, Client

class ViewTest():
    url =None
    function = None
    template = None
    status_code = 200
    redirect= None
    
    def setUp(self):
        # need a browser customer 
        self.client = Client()
        
    def get_data(self):
        """Generate a correct data
        """
        pass
    def test_root_url(self):
        """The view is the correct"""
        found = resolve(self.url)
        self.assertEqual(found.func.__name__, self.function.__name__)
        
    def test_return_correct_out(self):
        response = self.get_response()
        self.assertEqual(response.status_code,self.status_code)
        self.check_out(response)
      
    def uses_redirect(self, response):
        self.assertEqualI(response['location'], self.redirect)
    
    def check_out(self, response):
        if self.redirect is None:
            return self.check_html(response)  
        else:
            self.uses_redirect(response)   
            
    def check_html(self, response):
        # TODO: Cuando integren los html
        # self.is_working(response)
        self.uses_template(response)            
                      
    def uses_template(self, response):
        """Checking what templated are used"""
        print("respomse --------------",response)
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
        response = self.client.post(self.url, data=self.get_data())
        return response
                   
class GetViewTest(ViewTest):

    def get_response(self):
        response = self.client.get(self.url, data=self.get_data())
        return response
     

# TODO: Test de get contex data
# class HomePageTest(TestCase):
#     def test_environment_set_in_context(self):
#         request = RequestFactory().get('/')
#         view = HomeView()
#         view.setup(request)

#         context = view.get_context_data()
#         self.assertIn('environment', context)
    
    
    