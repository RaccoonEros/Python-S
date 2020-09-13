from collections import OrderedDict
import Items
import world


class Player:
    def __init__(self):
        self.inventory = [Items.Nudillo(),
                          Items.Daga(),
                          Items.LifePotion()]
        self.weapons = [Items.Nudillo(), Items.Daga()]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
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


    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


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