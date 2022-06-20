from django import views
from django.urls import path
from . import views
from .character.views import select_character_view
from .player.views import PlayerByUserView, PlayerView
from .beast.views import BeastByUserView, BeastView
from .battle import generar_batalla_aleatoria_view


urlpatterns=[
    path('',views.index, name='index'),
    path('register',views.register,name='register'),
    path('create_player/', views.create_player, name='create_player'),
    path('create_beast/',views.create_beast,name='create_beast'),
    path('create_battle/',views.create_battle,name='create_battle'),
    path('query1/',views.query1,name='query1'),
    path('query2/',views.query2,name='query2'),
    path('query3/',views.query3,name='query3'),
    path('query4/',views.query4,name='query4'),
    path('query5/',views.query5,name='query5'),
    path('query6/',views.query6,name='query6'),
    
    path('player_list/', PlayerByUserView.as_view(), name='player_list'),
    path('player/<int:player_id>/', PlayerView.as_view(), name='player'),
    path('beast_list/', BeastByUserView.as_view(), name='beast_list'),
    path('beast/<int:beast_id>/', BeastView.as_view(), name='beast'),
    path('<int:battle_id>/',select_character_view,name = 'list_player'),
    path('generar_batalla_aleatoria/<int:battle_id>/',generar_batalla_aleatoria_view, name = 'ran_battle_gen')
    
]