from skyrim.data.models import Spell

def get_all_spells():
    spell_list = Spell.objects.all()
    return spell_list.values()