from collections import OrderedDict
from player import Player
import world
import sys


def play():
    print("Pije Proyecto Cansado")
    world.parse_world_dsl()
    player = Player()
    inicio = True
    while player.still_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        if inicio == True:
            print(room.init_text())
            inicio = False

        print(room.intro_text())
        room.modify_player(player)
        if player.still_alive() and not player.victory:
            choose_action(room, player)
        elif not player.still_alive():
            print("Has muerto!")


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Accion Inválida!")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Escoger una accion: ")
    if player.inventory:
        action_adder(actions, 'I', player.print_inventory, "Mostrar Inventario")
    if isinstance(room, world.EnemyTile) and room.Monster.still_alive():
        action_adder(actions, 'A', player.attack, "Atacar")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'N', player.move_north, "Ir al Norte")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 'S', player.move_south, "Ir al Sur")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'E', player.move_east, "Ir al Este")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'O', player.move_west, "Ir al Oeste")
    if player.hp < 100:
        action_adder(actions, 'O', player.heal, "Objetos")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()