from typing import Dict
from webbrowser import get
from django.shortcuts import render, redirect
from django.http import HttpResponse
from skyrim.data.models import Battle,Place,PlaceType,Winner,BattleCharacter,Event
from skyrim.data.models import Character,Beast,Player, KnownSpell
from skyrim.data.models import DamageType, Attack, Spell,Blow,Race,PlayerRace
from skyrim.domain.forms import FormPlayer




def index(request):
    return render(request,'index.html')

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    return render(request,'register.html')

def create_player(request):
    races=PlayerRace.objects.all()
               
    if request.method=='POST':
        character=Character()
        character.character_name= request.POST['name']
        character.race_type= Race.objects.get(race_name=request.POST['race'])
        character.health_points=request.POST['health_points']
        character.save()

        player=Player()
        player.id_character= character
        player.save()
    
    return render(request,'create_player.html',{'races':races})

def create_beast(request):
    races=Race.objects.all()
    attacks=Attack.objects.all()

    if request.method=='POST':
        character=Character()
        character.character_name= request.POST['name']
        character.race_type= Race.objects.get(race_name=request.POST['race'])
        character.health_points=request.POST['health_points']
        character.save()

        beast=Beast()
        beast.id_character=character
        beast.id_attack=Attack.objects.get(attack_type=request.POST['attack'])
        beast.save()


    return render(request,'create_beast.html', {'races':races, 'attacks':attacks})

def create(request):
    name1 = request.POST['name']
    last_name1 = request.POST['last_name']
    return render(request,'create.html')

def create_battle(request):
    return render(request,'create_battle.html')

def query1(request):
    races=['Flame Atronach', 'Frost Atronach', 'Storm Atronach', 'Lurker', 'Seeker', 'Dwarven Ballista', 'Dwarven Centurion','Dwarven Sphere', 'Dwarven Spider','Giant', 'Chaurus','Falmer', 'Dragon', 'Spider', 'Troll', 'Werewolf', 'Ice Wraith', 'Hagravens', 'Draugr', 'Ghost', 'Skeleton']
    battles=[2, 9, 3, 5, 2, 3, 1,1,4,3,2,6,4,1,2,4,1,1,3,4,5]
    return render(request,'query1.html', {'races':races, 'battles':battles})

def query2(request):
    return render(request,'query2.html')

def query3(request):
    return render(request,'query3.html')

def query4(request):
    return render(request,'query4.html')

def query5(request):
    return render(request,'query5.html')

def query6(request):
    return render(request,'query6.html')


