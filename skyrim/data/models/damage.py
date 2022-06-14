from django.db import models
from django.db.models import Q

class DamageType(models.Model):
    type = models.CharField("damage type", max_length=15, unique=True)
    
    class Meta:
        app_label = 'myapp'

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
        app_label = 'myapp'
    
    def __str__(self) -> str:
        return "{} {}".format(self.damage_point, DamageType.objects.get(pk=self.attack_type.id).type)

class Spell(models.Model):
    spell_name = models.CharField("attack name", max_length=30, unique=True)
    id_spell = models.OneToOneField(Attack, verbose_name="spell id", primary_key=True, on_delete=models.CASCADE)

    class Meta:
        app_label = 'myapp'

    def  __str__(self) -> str:
        return self.spell_name

class Blow(models.Model):
    id_blow = models.OneToOneField(Attack, verbose_name="blow id", primary_key=True, on_delete=models.CASCADE)

    class Meta:
        app_label = 'myapp'

    def  __str__(self) -> str:
        return "{} {} blow".format(Attack.objects.get(pk=self.id_blow.id).damage_point, 
            DamageType.objects.get(pk=Attack.objects.get(pk=self.id_blow.id).attack_type.id).type)

class Race(models.Model):
    race_name = models.CharField("race name", max_length=30, unique=True)
    weakness = models.ForeignKey(DamageType, verbose_name="weakness", on_delete=models.CASCADE)

    class Meta:
        app_label='myapp'

    def  __str__(self) -> str:
        return self.race_name

class PlayerRace(models.Model):
    id_race = models.OneToOneField(Race, verbose_name="ID", primary_key= True, on_delete=models.CASCADE)

    class Meta:
        app_label='myapp'

    def  __str__(self) -> str:
        return Race.objects.get(pk=self.id_race.id).race_name