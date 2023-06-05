from skyrim.data.models import *
import datetime 


def Populate():
    #region DamageType
    fire = DamageType.objects.create(type = 'fire')
    air = DamageType.objects.create(type = 'air')
    stone = DamageType.objects.create(type = 'stone')
    water = DamageType.objects.create(type = 'water')
    poison = DamageType.objects.create(type = 'poison')
    #endregion 
  
    #region Attacks
    atk1 = Attack.objects.create(damage_point= 10,attack_type= fire )        
    atk2 = Attack.objects.create(damage_point= 10,attack_type= air )        
    atk3 = Attack.objects.create(damage_point= 10,attack_type= stone )        
    atk4 = Attack.objects.create(damage_point= 10,attack_type= water )        
    atk5 = Attack.objects.create(damage_point= 10,attack_type= poison )        
    
    atk6 = Attack.objects.create(damage_point=  15,attack_type= fire )        
    atk7 = Attack.objects.create(damage_point=  15,attack_type= air )        
    atk8 = Attack.objects.create(damage_point=  15,attack_type= stone )        
    atk9 = Attack.objects.create(damage_point=  15,attack_type= water )        
    atk10 = Attack.objects.create(damage_point= 15,attack_type= poison )
    
    atk11 = Attack.objects.create(damage_point= 20,attack_type= fire )        
    atk12 = Attack.objects.create(damage_point= 20,attack_type= air )        
    atk13 = Attack.objects.create(damage_point= 20,attack_type= stone )        
    atk14 = Attack.objects.create(damage_point= 20,attack_type= water )        
    atk15 = Attack.objects.create(damage_point= 20,attack_type= poison )        
    
    atk16 = Attack.objects.create(damage_point= 25,attack_type= fire )        
    atk17 = Attack.objects.create(damage_point= 25,attack_type= air )        
    atk18 = Attack.objects.create(damage_point= 25,attack_type= stone )        
    atk19 = Attack.objects.create(damage_point= 25,attack_type= water )        
    atk20 = Attack.objects.create(damage_point= 25,attack_type= poison )
    
    atk1_1 = Attack.objects.create(damage_point= 11,attack_type= fire )        
    atk2_1 = Attack.objects.create(damage_point= 11,attack_type= air )        
    atk3_1 = Attack.objects.create(damage_point= 11,attack_type= stone )        
    atk4_1 = Attack.objects.create(damage_point= 11,attack_type= water )        
    atk5_1 = Attack.objects.create(damage_point= 11,attack_type= poison )        
    
    atk6_1 = Attack.objects.create(damage_point=  16,attack_type= fire )        
    atk7_1 = Attack.objects.create(damage_point=  16,attack_type= air )        
    atk8_1 = Attack.objects.create(damage_point=  16,attack_type= stone )        
    atk9_1 = Attack.objects.create(damage_point=  16,attack_type= water )        
    atk10_1 = Attack.objects.create(damage_point= 16,attack_type= poison )
    
    atk11_1 = Attack.objects.create(damage_point= 21,attack_type= fire )        
    atk12_1 = Attack.objects.create(damage_point= 21,attack_type= air )        
    atk13_1 = Attack.objects.create(damage_point= 21,attack_type= stone )        
    atk14_1 = Attack.objects.create(damage_point= 21,attack_type= water )        
    atk15_1 = Attack.objects.create(damage_point= 21,attack_type= poison )  

    atk16_1 = Attack.objects.create(damage_point= 26,attack_type= fire )        
    atk17_1 = Attack.objects.create(damage_point= 26,attack_type= air )        
    atk18_1 = Attack.objects.create(damage_point= 26,attack_type= stone )        
    atk19_1 = Attack.objects.create(damage_point= 26,attack_type= water )        
    atk20_1 = Attack.objects.create(damage_point= 26,attack_type= poison )
    #endregion
   
    #region Spells
    spell1 = Spell(spell_name= 'little fireball', id_spell = atk1)
    spell1.save()
    spell2 = Spell(spell_name= 'little air blast', id_spell = atk2)
    spell2.save()
    spell3 = Spell(spell_name= 'little avalanche', id_spell = atk3)
    spell3.save()
    spell4 = Spell(spell_name= 'little wave', id_spell = atk4)
    spell4.save()
    spell5 = Spell(spell_name= 'little spit', id_spell = atk5)
    spell5.save()
    spell6 = Spell(spell_name= 'medium fireball', id_spell = atk6)
    spell6.save()
    spell7 = Spell(spell_name= 'medium air blast', id_spell = atk7)
    spell7.save()
    spell8 = Spell(spell_name= 'medium avalanche', id_spell = atk8)
    spell8.save()
    spell9 = Spell(spell_name= 'medium wave', id_spell = atk9)
    spell9.save()
    spell10 = Spell(spell_name='medium spit', id_spell = atk10)
    spell10.save()
    spell11 = Spell(spell_name= 'big fireball', id_spell = atk11)
    spell11.save()
    spell12 = Spell(spell_name= 'big air blast', id_spell = atk12)
    spell12.save()
    spell13 = Spell(spell_name= 'big avalanche', id_spell = atk13)
    spell13.save()
    spell14 = Spell(spell_name= 'big wave', id_spell = atk14)
    spell14.save()
    spell15 = Spell(spell_name= 'big spit', id_spell = atk15)
    spell15.save()
    spell16 = Spell(spell_name= 'colossal fireball', id_spell = atk16)
    spell16.save()
    spell17 = Spell(spell_name= 'colossal air blast', id_spell = atk17)
    spell17.save()
    spell18 = Spell(spell_name= 'colossal avalanche', id_spell = atk18)
    spell18.save()
    spell19 = Spell(spell_name= 'colossal wave', id_spell = atk19)
    spell19.save()
    spell20 = Spell(spell_name= 'colossal spit', id_spell = atk20)
    spell20.save()
    #endregion
  
    #region Blows
    blow1 = Blow(id_blow = atk1_1)
    blow1.save()
    blow2 = Blow(id_blow = atk2_1)
    blow2.save()
    blow3 = Blow(id_blow = atk3_1)
    blow3.save()
    blow4 = Blow(id_blow = atk4_1)
    blow4.save()
    blow5 = Blow(id_blow = atk5_1)
    blow5.save()
    blow6 = Blow(id_blow = atk6_1)
    blow6.save()
    blow7 = Blow(id_blow = atk7_1)
    blow7.save()
    blow8 = Blow(id_blow = atk8_1)
    blow8.save()
    blow9 = Blow(id_blow = atk9_1)
    blow9.save()
    blow10 = Blow(id_blow = atk10_1)
    blow10.save()
    blow11 = Blow(id_blow = atk11_1)
    blow11.save()
    blow12 = Blow(id_blow = atk12_1)
    blow12.save()
    blow13 = Blow(id_blow = atk13_1)
    blow13.save()
    blow14 = Blow(id_blow = atk14_1)
    blow14.save()
    blow15 = Blow(id_blow = atk15_1)
    blow15.save()
    blow16 = Blow(id_blow = atk16_1)
    blow16.save()
    blow17 = Blow(id_blow = atk17_1)
    blow17.save()
    blow18 = Blow(id_blow = atk18_1)
    blow18.save()
    blow19 = Blow(id_blow = atk19_1)
    blow19.save()
    blow20 = Blow(id_blow = atk20_1)
    blow20.save()
    #endregion
   
    #region races
    paladin = Race.objects.create(race_name = 'paladin',weakness = fire)
    archer = Race.objects.create(race_name = 'archer',weakness = air)
    warrior = Race.objects.create(race_name = 'warrior',weakness = stone)
    mage = Race.objects.create(race_name = 'mage',weakness = water)
    nigromant = Race.objects.create(race_name = 'nigromant',weakness = poison)

    dragon = Race.objects.create(race_name = 'dragon',weakness = fire)
    zombie = Race.objects.create(race_name = 'zombie',weakness = poison)
    tiny= Race.objects.create(race_name = 'tiny',weakness = stone)
    naga= Race.objects.create(race_name = 'naga',weakness = water)
    bird  = Race.objects.create(race_name = 'bird',weakness = air)
    
    PlayerRace.objects.create(id_race =paladin )
    PlayerRace.objects.create(id_race =mage )
    PlayerRace.objects.create(id_race =warrior )
    PlayerRace.objects.create(id_race =nigromant )
    PlayerRace.objects.create(id_race =archer )
    #endregion
  
    #region places
    place_type1 = PlaceType.objects.create(type = 'winter')
    place_type2 = PlaceType.objects.create(type = 'desert')
    place_type3 = PlaceType.objects.create(type = 'Montain')
    place_type4 = PlaceType.objects.create(type = 'beach')
    
    place1 = Place.objects.create(place_name = 'North',place_type= place_type1)
    place2 = Place.objects.create(place_name = 'Sahara',place_type= place_type2)
    place3 = Place.objects.create(place_name = 'Andes',place_type= place_type3)
    place4 = Place.objects.create(place_name = 'Egipto',place_type= place_type4)
    #endregion
   
    #region characters
    user,created = User.objects.get_or_create(email= 'example@gmail.com', username='user1', password='123')

    character1 = Character(character_name = 'character1',race_type = dragon,health_points = 500,id_client= user)
    character1.save()
    character2 = Character.objects.create(character_name = 'character2',race_type = bird,health_points = 700,id_client= user)
    character3 = Character.objects.create(character_name = 'character3',race_type = naga,health_points = 400,id_client= user)
    character4 = Character.objects.create(character_name = 'character4',race_type = tiny,health_points = 550,id_client= user)
    character5 = Character.objects.create(character_name = 'character5',race_type = zombie,health_points = 570,id_client= user)
    character6 = Character.objects.create(character_name = 'character6',race_type = paladin,health_points = 500,id_client= user)
    character7 = Character.objects.create(character_name = 'character7',race_type = warrior,health_points = 700,id_client= user)
    character8 = Character.objects.create(character_name = 'character8',race_type = mage,health_points = 400,id_client= user)
    character9 = Character.objects.create(character_name = 'character9',race_type = nigromant,health_points = 550,id_client= user)
    character10 = Character.objects.create(character_name = 'character10',race_type = archer,health_points = 570,id_client= user)
    #endregion
    
    #region battles
    battle1 = Battle.objects.create(place = place1, date = datetime.date(2022,2,16), time = datetime.time(12,30))  
    battle2 = Battle.objects.create(place = place2, date = datetime.date(2022,2,16), time = datetime.time(13))  
    battle3 = Battle.objects.create(place = place3, date = datetime.date(2022,2,16), time = datetime.time(13,30))  
    battle4 = Battle.objects.create(place = place4, date = datetime.date(2022,2,16), time = datetime.time(14))  
    
    battle1.fighters.add(character1)
    battle1.fighters.add(character2)
    
    Winner.objects.create(id_battle = battle2, winner = character2)
    #endregion
   
    #region beasts
    beast1 = Beast(id_character = character1,id_attack = blow1)
    beast1.save()
    beast1.place.add(place1)
    beast1.save()

    beast2 = Beast(id_character = character2,id_attack = blow2)
    beast2.save()
    beast2.place.add(place1)
    beast2.save()
    
    beast3 = Beast(id_character = character3,id_attack = blow3)
    beast3.save()
    beast3.place.add(place1)
    beast3.save()
    
    beast4 = Beast(id_character = character4,id_attack = blow4)
    beast4.save()
    beast4.place.add(place1)
    beast4.save()
    
    beast5 = Beast(id_character = character5,id_attack = blow5)
    beast5.save()
    beast5.place.add(place1)
    beast5.save()
    #endregion
   
    #region players
    player1 = Player(id_character = character6) 
    player1.save()
    player2 = Player(id_character = character7)
    player2.save()
    player3 = Player(id_character = character8)
    player3.save()
    player4 = Player(id_character = character9)
    player4.save()
    player5 = Player(id_character = character10)
    player5.save()
    #endregions
   
    #region knownspells
    knownspell1 = KnownSpell(id_player = player1, id_spell = spell1,spell_used = False)
    knownspell1.save()
    knownspell2 = KnownSpell.objects.create(id_player = player1, id_spell = spell2,spell_used = False)
    knownspell3 = KnownSpell.objects.create(id_player = player1, id_spell = spell3,spell_used = False)
    knownspell4 = KnownSpell.objects.create(id_player = player1, id_spell = spell4,spell_used = False)
    knownspell5 = KnownSpell.objects.create(id_player = player1, id_spell = spell5,spell_used = True)
    knownspell6 = KnownSpell.objects.create(id_player = player2, id_spell = spell3,spell_used = False)
    knownspell7 = KnownSpell.objects.create(id_player = player3, id_spell = spell3,spell_used = False)
    knownspell8 = KnownSpell.objects.create(id_player = player3, id_spell = spell1,spell_used = True)
    knownspell9 = KnownSpell.objects.create(id_player = player4, id_spell = spell3,spell_used = True)
    knownspell10 = KnownSpell.objects.create(id_player = player4, id_spell = spell7,spell_used = True)
    knownspell11 = KnownSpell.objects.create(id_player = player4, id_spell = spell4,spell_used = False)
    knownspell12 = KnownSpell.objects.create(id_player = player5, id_spell = spell3,spell_used = False)
    knownspell13 = KnownSpell.objects.create(id_player = player5, id_spell = spell1,spell_used = False)
    knownspell14 = KnownSpell.objects.create(id_player = player5, id_spell = spell6,spell_used = False)
    #endregion

    #region events
    event1 = Event(id_event = 1, id_battle = battle1,id_attacker = character1,id_damaged= character2,id_attack= atk1,health_points_before = 100,health_points_after = 80)
    event1.save()
    event2 = Event(id_event = 2, id_battle = battle1,id_attacker = character2,id_damaged= character3,id_attack= atk1,health_points_before = 100,health_points_after = 80)
    event2.save()
    
    #endregion
