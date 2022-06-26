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
from django.utils import timezone
from django.http.response import HttpResponseBadRequest


from django.urls import reverse_lazy

def index(request):
    return render(request,'index.html')

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    return render(request,'register.html')

def create_player_view(request):
    if request.method=='POST':
        player_id = create_player(
            request.POST['name'],
            request.POST['race_id'],
            request.POST['health_points'],
            request.user.id
        )
        # known_spell_list = request.POST.getlist('known_spell_list',None)
        known_spell_list = [2]
        if(known_spell_list == None or len(known_spell_list) == 0 or known_spell_list[0] == ''):
            return HttpResponseBadRequest("Para crear un player debes asignarle algun hechizo")
        add_several_known_spells_same_player_from_id(player_id, known_spell_list)
        
    race_list = get_all_player_races()
    spell_list = get_all_spells()
    return render(request,'create_player.html',{'race_list':race_list, 'spell_list':spell_list})

def create_beast_view(request):
    
    if request.method=='POST':
        place_id_list = request.POST.getlist('place',None)
        if(place_id_list == None or len(place_id_list) == 0 or place_id_list[0] == ''):
            return HttpResponseBadRequest("Para crear un player debes asignarle algun hechizo")
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

def create(request):
    name1 = request.POST['name']
    last_name1 = request.POST['last_name']
    return render(request,'create.html')



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


