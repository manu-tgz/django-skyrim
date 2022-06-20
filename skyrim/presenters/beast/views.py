from django.views.generic import ListView, TemplateView
from skyrim.domain.beast.queries import get_beast_list, get_beast

class BeastByUserView(ListView):
    template_name = "test.html"  
    
    def get(self, request, *args , **kwargs):
        self.queryset = get_beast_list(request.user.id)
        print(self.queryset)
        return super().get(request, *args, **kwargs) 
    
class BeastView(TemplateView):
    template_name = "test copy.html" 
    
    def get_context_data(self, **kwargs): 
        beast_id = kwargs.get('beast_id',0)
        beast = get_beast(beast_id) 
        context = {'id':beast.id,
                   'id_character':beast.id_character,
                   'id_attack': beast.id_attack,
                   'place': beast.place           
        }
        return context
         
    