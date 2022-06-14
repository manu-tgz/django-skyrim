from django.db import models
from django.db.models import Q
from .character import Character
from .damage import Spell


class PlaceType(models.Model):
    type = models.CharField("place type", max_length=30, unique=True)

    class Meta:
        app_label='myapp'
    
    def __str__(self) -> str:
        return self.type

class Place(models.Model):
    place_name = models.CharField("place name", max_length=30, unique=True)
    place_type = models.ForeignKey(PlaceType, verbose_name="place type", on_delete=models.CASCADE)
#   place_image = models.URLField("image", unique=True)

    class Meta:
        app_label='myapp'

    def __str__(self) -> str:
        return self.place_name


class Battle(models.Model):
    place = models.ForeignKey(Place, verbose_name="place", on_delete=models.CASCADE)
    date = models.DateField("date")
    time = models.TimeField("time")

    battle_constraint = models.UniqueConstraint(
        name="battle constraint",
        fields=['place', 'date', 'time']
    )

    class Meta:
        app_label='myapp'

class Winner(models.Model):
    id_battle = models.OneToOneField(Battle, verbose_name="battle id", primary_key=True, on_delete=models.CASCADE)
    winner = models.ForeignKey(Character, verbose_name="winner", on_delete=models.CASCADE)

class BattleCharacter(models.Model):
    battle = models.ForeignKey(Battle, verbose_name="battle id", on_delete=models.CASCADE)
    character = models.ForeignKey(Character, verbose_name="character", on_delete=models.CASCADE)

    battle_character_constraint = models.UniqueConstraint(
        name="battle character constraint",
        fields=['battle', 'character']
    )

    class Meta:
        app_label='myapp'

class Event(models.Model):
    id_event = models.IntegerField("event id")
    id_battle = models.ForeignKey(Battle, verbose_name="battle id", on_delete=models.CASCADE)
    id_attacker = models.ForeignKey(Character, verbose_name="attacker id", related_name="attacker", on_delete=models.CASCADE)
    id_damaged = models.ForeignKey(Character, verbose_name="damaged id", related_name="damaged", on_delete=models.CASCADE)
    id_spell = models.ForeignKey(Spell, verbose_name="spell id", null=True, on_delete=models.CASCADE)
    health_points_before = models.IntegerField("health point before")
    #health_points_after = models.IntegerField("health point after")
    
    event_constraint = models.UniqueConstraint(
        name="event constraint",
        fields=['id_event', 'id_battle']
    )

    class Meta:
        constraints = [models.CheckConstraint(
            name="health point before constraint",
            check=Q(health_points_before__gt=0)
        ),]
        app_label='myapp'