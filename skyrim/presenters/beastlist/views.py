from django.views.generic import ListView
from skyrim.domain.beast.queries import get_beast_list

class BeastByUserView(ListView):
    template_name = "test.html"  
    
    def get(self, request, *args , **kwargs):
        self.queryset = get_beast_list(request.user.id)
        print(self.queryset)
        return super().get(request, *args, **kwargs)  
    