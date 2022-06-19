from skyrim.data.models import Race

def get_all_races():
    result = Race.objects.all()
    return result.values()