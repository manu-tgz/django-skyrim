from operator import index
from random import randint
from skyrim.data.models import Battle
from skyrim.domain.character.classes import Character_for_Battle
from skyrim.domain.event.classes import Event_for_Battle
from skyrim.domain. event.operations import insert_several_events_same_battle
from skyrim.domain.battle.operations import set_winner, set_winner_from_id
from skyrim.domain.battle.queries import get_characters_obj_from_battle
from random import randint
from math import floor

def swap(arr, index_A, index_B):
    temp = arr[index_A]
    arr[index_A] = arr[index_B]
    arr[index_B] = temp

def select_random_subarray(arr,n):
    result = []
    length = len(arr)
    if(length == 1):
        return arr
    if(n <= length):
        for i in range(n):
            index = randint(i,length - 1)
            result.append(arr[index])
            swap(arr,i,index)
        return result
    else:
        return arr


def generar_batalla_aleatoria(id_battle):
    # Crear la lista de participantes activos y asignarle que puede usar
    active_fighters = []

    # obtener los datos
    #   - Por character
    #       * ataques con los tipos de ataque y damage
    #       * vida
    # almacenar los datos
    fighters = get_characters_obj_from_battle(id_battle)
    for character in fighters:
        cantidad_de_ataques = randint(1,3)
        character.ataques = select_random_subarray(character.ataques,cantidad_de_ataques)
        active_fighters.append(character)
    
    # simular batalla
    #   - llevar un numero de orden
    #   - cada ataque tiene un 95 o 105
    #   - 100 puntos extra de daño si el tipo de daño es igual a la debilidad
    
    step = 1
    event_list = []
    while(len(active_fighters) > 1 ):
    #   - seleccionar un par de vivos
        attacker_damaged = select_random_subarray(active_fighters, 2)
    #   - seleccionar un ataque aleatorio del atacante
        selected_attack = select_random_subarray(attacker_damaged[0].ataques,1)[0]
        damage = selected_attack.damage
    #   - seleccionar porciento aleatorio
        percent = 95 + randint(0,10)
        damage = floor(damage*percent/100)
    #   - comprobar debilidad
        if(selected_attack.attack_type == attacker_damaged[1].weakness_id):
            damage += 100
    #   - actualizar la vida
        attacker_damaged[1].hp -= damage
    #   - si es menor o igual que 0 retirar al participante de la batalla
        if(attacker_damaged[1].hp <= 0):
            active_fighters.remove(attacker_damaged[1])
        event = Event_for_Battle(step,
                                id_battle,
                                attacker_damaged[0].id_character,
                                attacker_damaged[1].id_character,
                                selected_attack.id,
                                attacker_damaged[1].hp + damage,
                                attacker_damaged[1].hp)
        event_list.append(event)
        step+=1
    insert_several_events_same_battle(event_list)
    set_winner_from_id(id_battle,active_fighters[0].id_character)
