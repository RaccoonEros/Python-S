from collections import OrderedDict
import Items
import world

####Creación basica del personaje, se que te toca a vos teruel pero ocupaba ir probando el
#sistema de combate, asi que las caracteristicas estan a lo pendejo, ya ahi lo retocas a
#forma que tenga bastante sentido.
class Player:
    def __init__(self):
        self.inventory = [Items.Nudillo(),
                          Items.Daga(),
                          Items.LifePotion()]
        self.weapons = [Items.Nudillo(), Items.Daga()]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.posx = 1.5
        self.posy = 0.5
        self.pasox = 0
        self.pasoy = 0
        self.hp = 100
        self.mp = 40
        self.defense = 4
        self.spd = 5
        self.exp = 0
        self.gold = 5
        self.victory = False

    def still_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        print("Oro: {}".format(self.gold))

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, Items.Consumable)]
        if not consumables:
            print("No tiene objetos que lo puedan curar")
            return

        for i, item in enumerate(consumables, 1):
            print("Escoja item para curar: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Elección inválida, intente de nuevo")
#Definicion de movimientos, actualmente solo son las armas que el personaje posee, pero
#espero luego cambiarlo por usar ataques con arma, o ataques magicos
    def moves(self):
        weapons = [item for item in self.inventory
                       if isinstance(item, Items.Weapon)]
        if not weapons:
            print("No tiene armas para usar")
            return

        for i, item in enumerate(weapons, 1):
            print("Escoja arma para atacar: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                atk = weapons[int(choice) - 1]
                damage = min(0, atk.damage)
                valid = True
                return atk
            except (ValueError, IndexError):
                print("Elección inválida, intente de nuevo")

#Mover la posicion del personaje segun el mapa#
    def move(self, dx, dy, mx, my):
        self.x += dx
        self.y += dy
        self.posx += mx
        self.posy += my
        self.pasox = mx
        self.pasoy = my

    def move_north(self):
        self.move(dx=0, dy=-1, mx=0, my=1)

    def move_south(self):
        self.move(dx=0, dy=1, mx=0, my=-1)

    def move_east(self):
        self.move(dx=1, dy=0, mx=1, my=0)

    def move_west(self):
        self.move(dx=-1, dy=0, mx=-1, my=0)

##Sistema de batalla del personaje, ya aqui involucre la defensa pero falta retocar de manera
#######que las peleas se sientan con bastante sentido y no duren poco o mucho tiempo
###Adeeemas, no le he añadido ahi estados para el personaje como envenenado, paralizado etc
    def attack(self):
        movement = self.moves()
        room = world.tile_at(self.x, self.y)
        Monster = room.Monster
        print("Usaste {} contra {}!".format(movement.name, Monster.name))
        if Monster.defense == 0:
            Monster.hp -= movement.damage
        else:
            Monster.hp -= movement.damage/Monster.defense
        if not Monster.still_alive():
            print("Has matado a {}!".format(Monster.name))
        else:
            print("El HP de {} es {}.".format(Monster.name, Monster.hp))