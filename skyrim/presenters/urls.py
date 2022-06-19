from django import views
from django.urls import path
from . import views
from skyrim.presenters.Select_Character_View.select_character_view import select_character_view

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
    path('player_list/',views.PlayerByUserView.as_view(), name='player_list'),
    path('beast_list/',views.BeastByUserView.as_view(), name='beast_list'),
    path('<int:battle_id>/',select_character_view,name = 'list_player'),
]