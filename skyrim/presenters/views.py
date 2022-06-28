from logging import raiseExceptions
from sys import implementation
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from skyrim.data.models import Battle,Place,PlaceType,Winner,BattleCharacter,Event
from skyrim.data.models import Character,Beast,Player, KnownSpell
from skyrim.data.models import DamageType, Attack, Spell,Blow,Race,PlayerRace
from skyrim.domain.attack.queries import get_all_blows
from skyrim.domain.forms import FormPlayer
from skyrim.domain.place.queries import get_all_places
from skyrim.domain.battle.operations import create_battle
from skyrim.domain.race.queries import get_all_player_races, get_all_races
from skyrim.domain.player.operations import create_player
from skyrim.domain.spell.queries import get_all_spells
from skyrim.domain.spell.operations import add_several_known_spells_same_player_from_id
from skyrim.domain.beast.operations import create_beast
from skyrim.domain.battle.queries import get_battle , get_winner, get_characters_from_battle, get_battle_stats
from skyrim.domain.event.queries import get_event_list
from skyrim.domain.character.queries import get_character_from_place, get_character_union_filters_by_user 
from skyrim.domain.user.operations import edit_user, create_user
from skyrim.domain.user.queries import get_user ,email_exist, username_exist
from django.utils import timezone
from django.http.response import HttpResponseBadRequest
from skyrim.domain.stats.statistics import BattleDuration, Beast_List, Rank_damage_player, Rank_n_players, Rank_n_attacks, used_spell, know_spell
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from skyrim.domain import forms
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth


from django.urls import reverse_lazy

from skyrim.domain.user.operations import edit_user
from skyrim.usecases.generar_batalla_aleatoria.operations import generar_batalla_aleatoria

@login_required
def index(request):
    return render(request,'index.html')

def register(request):   
    if request.method=='POST':
        username=request.POST['username1'] 
        first_name=request.POST['first_name'] 
        last_name=request.POST['last_name'] 
        email=request.POST['email'] 
        password1=request.POST['password1'] 
        password2=request.POST['password2'] 

        if password1==password2:
            if email_exist(email):
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif username_exist(username):
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                create_user(first_name,last_name,email,username,password1)
                return redirect('login')
        else:
            messages.info(request,'Password Not The Same')
            return redirect(register)

    return render(request,'register.html')



@login_required
def create_player_view(request):
    if request.method=='POST':
        player_id = create_player(
            request.POST['name'],
            request.POST['race_id'],
            request.POST['health_points'],
            request.user.id
        )
        known_spell_list = request.POST.getlist('pedro',None)
        
        
        if(known_spell_list == None or len(known_spell_list) == 0 or  known_spell_list[0] == ''):
            return HttpResponseBadRequest("You must select some spells")

        known_spell_list = known_spell_list[0].split(',')
    
        add_several_known_spells_same_player_from_id(player_id, known_spell_list)
        
    race_list = get_all_player_races()
    spell_list = get_all_spells()
    return render(request,'create_player.html',{'race_list':race_list, 'spell_list':spell_list})

@login_required
def create_beast_view(request):
    
    if request.method=='POST':
        place_id_list=request.POST.getlist('pedro', None)
        if(place_id_list == None or len(place_id_list) == 0 or  place_id_list[0] == ''):
            return HttpResponseBadRequest("You must select some spells")
        
        place_id_list=place_id_list[0].split(',')

        create_beast(
            character_name = request.POST['name'],
            race_type_id = request.POST['race'],
            health_points = request.POST['health_points'],
            id_client = request.user.id,
            id_blow = request.POST['blow'],
            place_id_list = place_id_list,
        )
    
    context = {}
    context['blow_list'] = get_all_blows()
    context['race_list'] = get_all_races()
    context['place_list'] = get_all_places()

    return render(request,'create_beast.html',context)


@login_required
def create_battle_view(request):
    value = request.GET.get('place',None)
    if value == None:
        place_list = get_all_places()
        context = {}
        context['place_list'] = place_list
        return render(request,'create_battle.html',context)
    else:
        today = timezone.now().date()
        now = timezone.now().time()
        place_id = value
        id = create_battle( place_id , today ,now)
        return redirect('select_character',battle_id = id)

@login_required
def battle_details_view(request,battle_id):
    context = {
        'fighters':get_characters_from_battle(battle_id),
        'stats':get_battle_stats(battle_id),
        'battle':get_battle(battle_id),
        'winner':get_winner(battle_id)
        }
    return render(request,'battle_details.html',context)

@login_required
def query1(request):
    races= Beast_List()
    return render(request,'query1.html', {'races':races})

@login_required
def query2(request):
    players=Rank_n_players(10)
    return render(request,'query2.html', {'players':players})

@login_required
def query3(request):
    battles=BattleDuration()
    return render(request,'query3.html', {'battle_list':battles})

@login_required
def query4(request):
    players=Rank_damage_player()
    return render(request,'query4.html', {'players':players})

@login_required
def query5(request):
    spells=Rank_n_attacks(10)
    return render(request,'query5.html', {'spells':spells})

@login_required
def query6(request):
    used_spells=used_spell()
    known_spells=know_spell()
    return render(request,'query6.html', {'used':used_spells, 'known': known_spells})

@login_required
def user_profile(request):
    context = {}
    id=request.user.id
    user=get_user(id)
    context['my_user'] = user
    if request.method =='POST':
        context['from_operation'] = False
        username=request.POST['username'] 
        first_name=request.POST['firstName'] 
        last_name=request.POST['lastName'] 
        email=request.POST['email'] 
        password1=request.POST['password1'] 
        password2=request.POST['password2'] 

        if password1==password2:
            if email_exist(email) and user['email']!=email:
                messages.info(request,'Email Already Used')
                context['from_operation'] = True
             
            elif username_exist(username) and user['username']!=username:
                messages.info(request,'Username Already Used')
                context['from_operation'] = True
                
            elif username == "":
                messages.info(request,'Empty username not allowed')
                context['from_operation'] = True

            elif password1 == "":
                messages.info(request,'Empty password not allowed')
                context['from_operation'] = True

            else:
                edit_user(request,id,first_name,last_name,email, username, password1)

                
        else:
            messages.info(request,'Password Not The Same')
            context['from_operation'] = True
            
    id=request.user.id
    user=get_user(id)
    context['my_user'] = user
    return render(request,'user_profile.html',context)

def user_characters(request):
    value = request.GET.get('query',None)
    if(value == ""):
        value = None
    character_list = get_character_union_filters_by_user(request.user.id, value)
    return render(request,"user_characters.html",{'character_list':character_list})

def login(request):
    return render(request,'login.html')

@login_required
def tables(request):
    return render(request, 'tables.html')
