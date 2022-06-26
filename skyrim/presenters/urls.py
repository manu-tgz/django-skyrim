from django import views
from django.urls import path
from . import views
from .character.views import select_character_view
from .player.views import PlayerByUserView, PlayerView
from .beast.views import BeastByUserView, BeastView
from .battle.generar_batalla_aleatoria_view import generar_batalla_aleatoria_view
from django.contrib.auth.views import LoginView, logout_then_login
from atexit import register
from unittest.mock import patch

urlpatterns=[    
    path('',views.index, name='login'),
    path('register',views.register,name='register'),
    path('create_player/', views.create_player_view, name='create_player'),
    path('create_beast/',views.create_beast_view,name='create_beast'),
    path('create_battle/',views.create_battle_view,name='create_battle'),
    path('query1/',views.query1,name='query1'),
    path('query2/',views.query2,name='query2'),
    path('query3/',views.query3,name='query3'),
    path('query4/',views.query4,name='query4'),
    path('query5/',views.query5,name='query5'),
    path('query6/',views.query6,name='query6'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('index',views.index,name='index'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('battle_details/<int:battle_id>',views.battle_details_view, name='battle_details'),
    path('tables',views.tables, name='tables'),
    path('user_characters/',views.user_characters, name = 'user_characters'),
    path('player_list/', PlayerByUserView.as_view(), name='player_list'),
    path('player/<int:player_id>/', PlayerView.as_view(), name='player'),
    path('beast_list/', BeastByUserView.as_view(), name='beast_list'),
    path('beast/<int:beast_id>/', BeastView.as_view(), name='beast'),
    path('<int:battle_id>/',select_character_view,name = 'select_character'),
    path('generar_batalla_aleatoria/<int:battle_id>/',generar_batalla_aleatoria_view, name = 'ran_battle_gen'),
    
]