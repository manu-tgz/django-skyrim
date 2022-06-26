from skyrim.data.models import Battle
from django.shortcuts import render, redirect
from skyrim.domain.race.queries import get_all_races
from skyrim.domain.user.queries import get_all_users
from skyrim.domain.character.queries import get_character_from_place
from skyrim.domain.battle.queries import get_characters_from_battle, get_battle
from skyrim.domain.battle.operations import remove_character_in_battle_from_id ,register_characters_in_battle_from_id
from skyrim.usecases.generar_batalla_aleatoria.operations import generar_batalla_aleatoria

def select_character_view(request, battle_id):
    battle = get_battle(battle_id)
    
    #Adding and removing from battle

    value = request.GET.getlist('register_fighter',None)
    if(not (value == None or len(value) == 0 or value[0] == "")):
        register_characters_in_battle_from_id(battle_id, value)
    
    value = request.GET.getlist('remove_fighter',None)
    if(not (value == None or len(value) == 0 or value[0] == "")):
        remove_character_in_battle_from_id(battle_id,value)

    #building query
    query = {}
    query['place_id'] = battle['place_id']
    query['battle_id'] = battle_id
    for key in request.GET.dict().keys():
        query[key] = request.GET.getlist(key,None)
    
    #getting the action
    start = False
    value = query.get('page',None)
    if(value == None or len(value) == 0 or value[0] == ""):
        query['page'] = [1]
    else:
        value = query.get('action',None)
        if(not(value == None or len(value) == 0 or value[0] == "")):
            if value[0] == 'next':
                query['page'] = [str(int(query['page'][0]) + 1)]
            
            elif value[0] == 'preview':
                query['page'] = [str(int(query['page'][0]) - 1)]

            elif value[0] == 'filter':
                query['page'][0] = '1'

            elif value[0] == 'start':
                start = True


    if(start):
        generar_batalla_aleatoria(battle_id)
        return redirect('battle_details',battle_id = battle_id)
    else:
        #building context
        context = {}
        context['users_list'] = get_all_users()
        context['races_list'] = get_all_races()
        result = get_character_from_place(query,7) 
        context['character_list'] = result[1:]
        context['fighters_list'] = get_characters_from_battle(battle_id)
        context['pagination'] = result[0]
        context['id_battle'] = battle_id
        return render(request, "select_character.html",context)
    