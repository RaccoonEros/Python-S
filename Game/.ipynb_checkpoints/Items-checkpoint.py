#####Nuevamente teruel, me disculpo que tire aqui esto si a vos te toca lo de los items
#####Pero la misma vaina, probaba el sistema de pelea y necesitaba ver que escogiera
#####Arma, y se pudiera curar y esas vainas. Todavia no he tirado ahi que funcione la
#####pocion de mana, pero porque no he tirado ningun ataque o movimiento magico que
####gaste mana.

class Weapon:
    def __init__(self):
        raise NotImplementedError("Objeto perteneciente a armas creado con vacios")

    def __str__(self):
        return "{} ({} Daño)" .format(self.name, self.damage)


class Nudillo(Weapon):
    def __init__(self):
        self.name = "Nudillo"
        self.description = "Nudillos de metal para golpe directo"
        self.damage = 25
        self.value = 1


class Daga(Weapon):
    def __init__(self):
        self.name = "Daga"
        self.description = "Una daga pequeña"
        self.damage = 50
        self.value = 20


class EspadaHierro(Weapon):
    def __init__(self):
        self.name = "Espada de Hierro"
        self.description = "Una espada básica"
        self.damage = 20
        self.value = 100


class Consumable:
    def __init__(self):
        raise NotImplementedError("Objeto Consumable creado vacio")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class LifePotion(Consumable):
    def __init__(self):
        self.name = "Pocion de Vida"
        self.healing_value = 50
        self.value = 60

class PanViejo(Consumable):
    def __init__(self):
        self.name = "Pan Viejo"
        self.healing_value = 10
        self.value = 60

class BotellaAgua(Consumable):
    def __init__(self):
        self.name = "Botella de Agua"
        self.healing_value = 20
        self.value = 60

class MagicPotion(Consumable):
    def __init__(self):
        self.name = "Pocion de Magia"
        self.magic_value = 50
        self.value = 60
