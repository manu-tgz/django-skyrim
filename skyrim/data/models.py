from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class DamageType(models.Model):
    type = models.CharField("damage type", max_length=15, unique=True)
    
    def __str__(self) -> str:
        return self.type

class Attack(models.Model):
    damage_point = models.IntegerField("damage point")
    attack_type = models.ForeignKey(DamageType, verbose_name="attack type", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="damage attack point",
                check=Q(damage_point__gt=0)
            ),
            models.UniqueConstraint(
                name="unique attack id",
                fields=['damage_point', 'attack_type']
            ),
        ]
    
    def __str__(self) -> str:
        return "{} {}".format(self.damage_point, DamageType.objects.get(pk=self.attack_type.id).type)

class Spell(models.Model):
    spell_name = models.CharField("attack name", max_length=30, unique=True)
    id_spell = models.OneToOneField(Attack, verbose_name="spell id", primary_key=True, on_delete=models.CASCADE)

    def  __str__(self) -> str:
        return self.spell_name

class Blow(models.Model):
    id_blow = models.OneToOneField(Attack, verbose_name="blow id", primary_key=True, on_delete=models.CASCADE)

    def  __str__(self) -> str:
        return "{} {} blow".format(Attack.objects.get(pk=self.id_blow.id).damage_point, 
            DamageType.objects.get(pk=Attack.objects.get(pk=self.id_blow.id).attack_type.id).type)

class Race(models.Model):
    race_name = models.CharField("race name", max_length=30, unique=True)
    weakness = models.ForeignKey(DamageType, verbose_name="weakness", on_delete=models.CASCADE)

    def  __str__(self) -> str:
        return self.race_name

class PlayerRace(models.Model):
    id_race = models.OneToOneField(Race, verbose_name="ID", primary_key= True, on_delete=models.CASCADE)

    def  __str__(self) -> str:
        return Race.objects.get(pk=self.id_race.id).race_name



class Character(models.Model):
    character_name = models.CharField("character name", max_length=30, unique=True)
    race_type = models.ForeignKey(Race, verbose_name="race type", on_delete=models.CASCADE)
    health_points = models.IntegerField("health points")
    id_client = models.ForeignKey(User, verbose_name="user id", on_delete=models.CASCADE)


    class Meta:
        constraints = [models.CheckConstraint(
            name="health point constraint",
            check=Q(health_points__gt=0)
        ),]

    def __str__(self) -> str:
        return self.character_name

class Beast(models.Model):
    id_character = models.ForeignKey(Character, verbose_name="character id", on_delete=models.CASCADE)
    id_attack = models.ForeignKey(Blow, verbose_name="attack id", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return Character.objects.get(pk=self.id_character.id).character_name

class Player(models.Model):
    id_character = models.ForeignKey(Character, verbose_name="Character id", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return Character.objects.get(pk=self.id_character.id).character_name

class KnownSpell(models.Model):
    id_player = models.ForeignKey(Player, verbose_name="player id", on_delete=models.CASCADE)
    id_spell = models.ForeignKey(Spell, verbose_name="spell id", on_delete=models.CASCADE)
    spell_used = models.BooleanField("spell used")

    class Meta:
        constraints =[models.UniqueConstraint(
            name="know constraint",
            fields=['id_player', 'id_spell']
            ),]

    def __str__(self) -> str:
        return Spell.objects.get(pk=self.id_spell.id).spell_name


class PlaceType(models.Model):
    type = models.CharField("place type", max_length=30, unique=True)

    def __str__(self) -> str:
        return self.type

class Place(models.Model):
    place_name = models.CharField("place name", max_length=30, unique=True)
    place_type = models.ForeignKey(PlaceType, verbose_name="place type", on_delete=models.CASCADE)
#   place_image = models.URLField("image", unique=True)

    def __str__(self) -> str:
        return self.place_name

class BeastLive(models.Model):
    id_beast = models.ForeignKey(Beast, verbose_name="beast id", on_delete=models.CASCADE)
    id_place = models.ForeignKey(Place, verbose_name="place id", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} live in {}".format(
            Character.objects.get(pk=Beast.objects.get(pk=self.id_beast.id).id).character_name,
            Place.objects.get(pk=self.id_place.id).place_name)

class Battle(models.Model):
    place = models.ForeignKey(Place, verbose_name="place", on_delete=models.CASCADE)
    date = models.DateField("date")
    time = models.TimeField("time")

    class Meta:
        constraints =[models.UniqueConstraint(
        name="battle constraint",
        fields=['place', 'date', 'time']
        ),]

    def __str__(self) -> str:
        return "battle {} in {}".format(self.pk, Place.objects.get(pk=self.place.id).place_name)

class Winner(models.Model):
    id_battle = models.OneToOneField(Battle, verbose_name="battle id", primary_key=True, on_delete=models.CASCADE)
    winner = models.ForeignKey(Character, verbose_name="winner", on_delete=models.CASCADE)

    def  __str__(self) -> str:
        return "the winner in the battle {} is {}".format(self.id_battle, Character.objects.get(pk=self.winner.id).character_name)

class BattleCharacter(models.Model):
    battle = models.ForeignKey(Battle, verbose_name="battle id", on_delete=models.CASCADE)
    character = models.ForeignKey(Character, verbose_name="character", on_delete=models.CASCADE)

    class Meta:
        constraints=[models.UniqueConstraint(
        name="battle character constraint",
        fields=['battle', 'character']
        ),]
    
    def  __str__(self) -> str:
        return "{} fight in the battle {}".format(Character.objects.get(pk=self.character.id).character_name, self.battle)

class Event(models.Model):
    id_event = models.IntegerField("event id")
    id_battle = models.ForeignKey(Battle, verbose_name="battle id", on_delete=models.CASCADE)
    id_attacker = models.ForeignKey(Character, verbose_name="attacker id", related_name="attacker", on_delete=models.CASCADE)
    id_damaged = models.ForeignKey(Character, verbose_name="damaged id", related_name="damaged", on_delete=models.CASCADE)
    id_attack = models.ForeignKey(Attack, verbose_name="attack id", on_delete=models.CASCADE)
    health_points_before = models.IntegerField("health point before")

    class Meta:
        constraints = [models.CheckConstraint(
            name="health point before constraint",
            check=Q(health_points_before__gt=0)
        ),models.UniqueConstraint(
        name="event constraint",
        fields=['id_event', 'id_battle']
        ),]
    
    def  __str__(self) -> str:
        return "{} attack for {} {} damage to {}".format(
            Character.objects.get(pk=self.id_attacker.id).character_name,
            Attack.objects.get(pk=self.id_attack.id).damage_point,
            Attack.objects.get(pk=self.id_attack.id).attack_type,
            Character.objects.get(pk=self.id_damaged.id).character_name,
            )
