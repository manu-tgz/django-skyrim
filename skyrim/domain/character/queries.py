from django.core.paginator import Paginator
from skyrim.data.models import Character, Battle
from django.db.models import Q, Value, CharField



def get_character_from_place(query, paginate_by = None):
    result = Character.objects.all()
    #general filters
    value = query.get('id',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(id = value[0])
        
    value = query.get('character_name__icontains',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(character_name__icontains = value[0])
    
    value = query.get('health_points__gte',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(health_points__gte = value[0])
    
    value = query.get('health_points__lte',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(health_points__lte = value[0])
    
    value = query.get('id_client',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(id_client = value[0])
    
    value = query.get('race_type',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(race_type__id = value[0])
    
    fighters = None
    battle_id = query.get('battle_id',None)
    if(not battle_id == None):
        battle = Battle.objects.get(id = battle_id)
        fighters = battle.fighters.all()
    #type filters

    players = None
    beasts = None
    type_value = query.get('type', None)

    if(type_value == None or len(type_value) == 0 or type_value[0] == '' or type_value[0] == 'player'):
        players = result.exclude(player = None)
        players = players.annotate(type = Value('player', output_field= CharField()))

    if(type_value == None or len(type_value) == 0 or type_value[0] == '' or type_value[0] == 'beast'):
        value = query.get('place_id',None)
        if(value == None):
            beasts = result.exclude(beast = None)
        else:
            beasts = result.filter(beast__place__id = value)
        beasts = beasts.annotate(type = Value('beast', output_field= CharField()))

    if(type_value == None or len(type_value) == 0  or type_value[0] == ""):
        result = players.union(beasts)
    elif type_value[0] == 'player':
        result = players
    elif type_value[0] == 'beast':
        result = beasts
    else:
        raise Exception('No existe el tipo ' + type_value)
    
    # añadiendo paginacion

    result = result.order_by('id')
    dict_arr_result = []

    if(not paginate_by == None):
        dict_arr_result.append({})
        paginator = Paginator(result,paginate_by)
        value = query.get('page',None)
        if(value == None or len(value) == 0 or value[0] == ""):
            value = 1
        else:
            value = int(value[0])
        if(1 <= value <= paginator.num_pages):
            result = paginator.page(value)
            dict_arr_result[0]['page'] = value
            dict_arr_result[0]['has_previous'] = result.has_previous()
            dict_arr_result[0]['has_next'] = result.has_next()
            result = result.object_list
        else:
            result = []
            dict_arr_result[0]['wrong_page'] = True

    # Serializando
    for item in result:
        current = {
            'id':item.id,
            'Nombre':item.character_name,
            'Raza_label':item.race_type.race_name,
            'Raza_key':item.race_type.id,
            'Puntos_de_Vida':item.health_points,
            'Creador_label':item.id_client.username,
            'Creador_key':item.id_client.id,
            'Tipo':item.type,
        }
        if(not battle_id == None):
            current['in_battle'] = item in fighters
            
        dict_arr_result.append(current)
    return dict_arr_result
    

def get_character_union_filters_by_user(id_user, value = None):
    user_char = Character.objects.filter(id_client = id_user)
    result = None
    user_beast = user_char.exclude(player = None)
    user_player = user_char.exclude(beast = None)
    if(not value == None):
        result = user_char.filter(character_name__startswith = value)
        temp = user_char.filter(race_type__race_name__startswith = value)
        result = result.union(temp)
        if(value.isdigit()):
            temp = user_char.filter(health_points = int(value))
        result = result.union(temp)
        temp = None
        if("player".startswith(value)):
            temp = user_player
        elif"beast".startswith(value):
            temp = user_beast
        if(not temp == None):
            result = result.union(temp)
    else:
        result = user_char
    final_result = []
    for item in result:
        current = {
            'id':item.id,
            'Nombre':item.character_name,
            'Raza_label':item.race_type.race_name,
            'Raza_key':item.race_type.id,
            'Puntos_de_Vida':item.health_points,
        }
        if(item in user_beast):
            current['Tipo'] = 'beast'
        else:
            current['Tipo'] = 'player'
        final_result.append(current)

    return final_result