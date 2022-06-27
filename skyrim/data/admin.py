from django.contrib import admin
from . import models

admin.site.register(models.Character)
admin.site.register(models.Beast)
admin.site.register(models.Race)
admin.site.register(models.Blow)
admin.site.register(models.Attack)
admin.site.register(models.DamageType)
admin.site.register(models.Place)
admin.site.register(models.PlaceType)
admin.site.register(models.Player)
admin.site.register(models.Battle)
admin.site.register(models.PlayerRace)
admin.site.register(models.KnownSpell)
admin.site.register(models.Spell)
admin.site.register(models.Winner)