from skyrim.data.models import Place

def get_all_places():
    place_list = Place.objects.all()
    result = []
    for place in place_list:
        current_dict = {}
        current_dict['id'] = place.id
        current_dict['name'] = place.place_name
        current_dict['type_id'] = place.place_type.id
        current_dict['type_name'] = place.place_type.type
        result.append(current_dict)
    return result

    