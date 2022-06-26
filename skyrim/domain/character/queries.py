
from pickle import TRUE
from django.core.paginator import Paginator
from skyrim.data.models import Character
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
    
    value = query.get('not_in_battle_id',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(race_type__id = value[0])
    
    value = query.get('in_battle_id',None)
    if(not value == None and not len(value) == 0 and not value[0] == ""):
        result = result.filter(race_type__id = value[0])
    

    #type filters

    players = None
    beasts = None
    type_value = query.get('type', None)

    if(type_value == None or len(type_value) == 0 or value[0] == '' or type_value[0] == 'player'):
        players = result.exclude(player = None)
        players = players.annotate(type = Value('player', output_field= CharField()))

    if(type_value == None or len(type_value) == 0 or value[0] == '' or type_value[0] == 'beast'):
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
            dict_arr_result[0]['has_previous'] = result.has_previous()
            dict_arr_result[0]['has_next'] = result.has_next()
            result = result.object_list
        else:
            result = []
            dict_arr_result[0]['wrong_page'] = TRUE

    # Serializando
    for item in result:
        dict_arr_result.append({
            'Nombre':item.character_name,
            'Raza_label':item.race_type.race_name,
            'Raza_key':item.race_type.id,
            'Puntos_de_Vida':item.health_points,
            'Creador_label':item.id_client.username,
            'Creador_key':item.id_client.id,
            'Tipo':item.type,
        })
    return dict_arr_result
    