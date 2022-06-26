from django.http.response import HttpResponseBadRequest
from skyrim.domain.battle.operations import register_characters_in_battle_from_id
from skyrim.usecases.generar_batalla_aleatoria.operations import generar_batalla_aleatoria

def generar_batalla_aleatoria_view(request, id_battle):
    participantes = request.GET.getlist('contestant',None)
    if(participantes == None or len(participantes) == 0 or participantes[0] == ''):
        return HttpResponseBadRequest()
    
    register_characters_in_battle_from_id(id_battle,participantes)
    generar_batalla_aleatoria(id_battle,participantes)
    

        
        