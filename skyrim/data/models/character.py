from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from .damage import Race, Attack, Spell

class Character(models.Model):
    character_name = models.CharField("character name", max_length=30, unique=True)
    race_type = models.ForeignKey(Race, verbose_name="race type", on_delete=models.CASCADE)
    health_points = models.IntegerField("health points")

    class Meta:
        constraints = [models.CheckConstraint(
            name="health point constraint",
            check=Q(health_points__gt=0)
        ),]
        app_label='myapp'

    def __str__(self) -> str:
        return self.character_name

class Beast(models.Model):
    id_character = models.ForeignKey(Character, verbose_name="character id", on_delete=models.CASCADE)
    id_attack = models.ForeignKey(Attack, verbose_name="attack id", on_delete=models.CASCADE)

    class Meta:
        app_label='myapp'

    def __str__(self) -> str:
        return Character.objects.get(pk=self.id_character.id).character_name

class Player(models.Model):
    id_character = models.ForeignKey(Character, verbose_name="Character id", on_delete=models.CASCADE)
    
    class Meta:
        app_label='myapp'

    def __str__(self) -> str:
        return Character.objects.get(pk=self.id_character.id).character_name

class KnownSpell(models.Model):
    id_player = models.ForeignKey(Player, verbose_name="player id", on_delete=models.CASCADE)
    id_spell = models.ForeignKey(Spell, verbose_name="spell id", on_delete=models.CASCADE)
    spell_used = models.BooleanField("spell used")

    know_constraint = models.UniqueConstraint(
        name="know constraint",
        fields=['id_player', 'id_spell']
    )

    class Meta:
        app_label='myapp'

    def __str__(self) -> str:
        return Spell.objects.get(pk=self.id_spell.id).spell_name