from collections import OrderedDict
import Items
import world
import sys
import os

####Creación basica del personaje, se que te toca a vos teruel pero ocupaba ir probando el
#sistema de combate, asi que las caracteristicas estan a lo pendejo, ya ahi lo retocas a
#forma que tenga bastante sentido.
class Player:
    def __init__(self):
        self.inventory = [Items.Nudillo(), Items.Daga(), Items.Relampago(), Items.Llamarada(), Items.EspadaHierro(), Items.LifePotion(), Items.LifePotion(), Items.LifePotion(), Items.LifePotion(), Items.MagicPotion(), Items.MagicPotion(), Items.MagicPotion()]
        self.weapons = [Items.Nudillo(), Items.Daga()]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.posx = 1.5
        self.posy = 0.5
        self.pasox = 0
        self.pasoy = 0
        self.hp = 100
        self.mp = 40
        self.magicdefense = 5
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
                if to_eat.healing_value > 0:
                    self.hp = min(100, self.hp + to_eat.healing_value)
                    self.inventory.remove(to_eat)
                    print("Valor de HP: {}".format(self.hp))
                    valid = True
                elif to_eat.magic_value > 0:
                    self.mp = min(100, self.hp + to_eat.magic_value)
                    self.inventory.remove(to_eat)
                    print("Valor de MP: {}".format(self.hp))
                    valid = True
            except (ValueError, IndexError):
                print("Elección inválida, intente de nuevo")
#Definicion de movimientos, actualmente solo son las armas que el personaje posee, pero
#espero luego cambiarlo por usar ataques con arma, o ataques magicos
    def moves(self):
        mov = [item for item in self.inventory
                       if isinstance(item, Items.MovAtak)]
        if not mov:
            print("No tiene ataques para usar")
            return

        for i, item in enumerate(mov, 1):
            print("Escoja movimiento de ataque: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                atk = mov[int(choice) - 1]
                if atk.damage > 0:
                    damage = min(0, atk.damage)
                    valid = True
                    return atk
                elif atk.magicdamage > 0:
                    damage = min(0, atk.magicdamage)
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
        if movement.damage > 0:
            if Monster.defense == 0:
                Monster.hp -= movement.damage
            else:
                Monster.hp -= movement.damage/Monster.defense
        elif movement.magicdamage > 0 :
            if Monster.magdefense == 0:
                Monster.hp -= movement.magicdamage
                self.mp = min(100, self.hp - movement.mpcost)
                print("Valor de MP: {}".format(self.hp))
            else:
                Monster.hp -= movement.magicdamage/Monster.magdefense
                self.mp = min(100, self.hp - movement.mpcost)
                print("Valor de MP: {}".format(self.hp))
        if not Monster.still_alive():
            print("Has matado a {}!".format(Monster.name))
        else:
            print("El HP de {} es {}.".format(Monster.name, Monster.hp))
    
    def pausa(self):
        print("#######################################")
        print("               -PAUSA-                 ")
        print("---------------------------------------")
        print("   -[r] Reanudar juego")
        print("   -[s] Salvar partida")
        print("   -[q] Salir del juego")
        comando=input("> ")
        if comando=="r" or comando=="R" :
            pass
        elif comando=="s" or comando=="S" :
            #LLamar funcion para guardara partida
            print("Partida guardada")
        elif comando=="q" or comando=="Q" :
            print("#############################################################################")
            print("Si no ha salvado su partida, se le recomienda salvar antes de salir del juego")
            print("#############################################################################")
            print("                    ¿Desea abandonar el juego?")
            print("                    -[y] Si")
            print("                    -[n] No")
            respuesta=input("> ")
            if respuesta=="y" or respuesta=="Y":
                sys.exit()  
            elif respuesta=="n" or respuesta=="N" :
                pass
            while respuesta not in ["y","n"]:
                print("Por favor ingresar un comando valido (y:Si, n:No)")
                respuesta=input("> ")
                if respuesta=="y":
                    sys.exit()  
                elif respuesta=="n":
                    pass
        while comando not in ["r","R","s","S","q","Q"]:
            print("Por favor ingresar un comando válido (r:reanudar juego, s:salvar partida, q, salir del juego")
            comando=input("> ")
            if comando=="r" or comando=="R" :
                break
            elif comando=="s" or comando=="S" :
                #LLamar funcion para guardara partida
                print("Partida guardada")
            elif comando=="q" or comando=="Q" :
                print("#############################################################################")
                print("Si no ha salvado su partida, se le recomienda salvar antes de salir del juego")
                print("#############################################################################")
                print("                    ¿Desea abandonar el juego?")
                print("                    -[y] Si")
                print("                    -[n] No")
                respuesta=input("> ")
                if respuesta=="y" or respuesta=="Y" :
                    sys.exit()  
                elif respuesta=="n" or respuesta=="N":
                    break
                while respuesta not in ["y","Y","n","N"]:
                    print("Por favor ingresar un comando valido (y:Si, n:No)")
                    respuesta=input("> ")
                    if respuesta=="y" or respuesta=="Y" :
                        sys.exit()  
                    elif respuesta=="n" or respuesta=="N" :
                        pass
                if(respuesta=="n"):
                    break