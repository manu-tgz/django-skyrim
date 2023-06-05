from django.urls import path
from .generar_batalla_aleatoria_view import generar_batalla_aleatoria_view

urlpatterns = [
    path('generar_batalla_aleatoria/<int:battle_id>/',generar_batalla_aleatoria_view, name = 'ran_battle_gen')
]
