from django.views.generic import ListView
from skyrim.domain.player.queries import get_player_list

class PlayerByUserView(ListView): 
    template_name = "test.html" 
    
    def get(self, request, *args , **kwargs):
        self.queryset = get_player_list(request.user.id)
        return super().get(request, *args, **kwargs)