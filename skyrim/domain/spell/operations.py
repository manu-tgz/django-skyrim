from skyrim.data.models import KnownSpell,Spell, Player

def add_several_known_spells_same_player_from_id(player_id, spell_id_list):
    player = Player.objects.get(id = player_id)
    add_several_knwon_spells_same_player(player,spell_id_list)

def add_several_knwon_spells_same_player(player,spell_id_list):
    for spell_id in spell_id_list:
        spell = Spell.objects.get(id_spell = spell_id)
        ks = KnownSpell(
            id_player = player,
            id_spell = spell,
            spell_used = False)
        ks.save()