from django.views.generic import TemplateView, ListView, DetailView
from skyrim.domain.player.queries import get_player_list, get_player

class PlayerByUserView(ListView): 
    template_name = "test.html" 
    
    def get(self, request, *args , **kwargs):
        print(self.kwargs)
        self.queryset = get_player_list(request.user.id)
        return super().get(request, *args, **kwargs)

class PlayerView(TemplateView):
    template_name = "test copy.html" 
    
    def get_context_data(self, **kwargs): 
        player_id = kwargs.get('player_id',0)
        player = get_player(player_id) 
        context = {'id':player.id,'id_character':player.id_character }
        return context
        
