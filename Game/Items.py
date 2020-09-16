#####Nuevamente teruel, me disculpo que tire aqui esto si a vos te toca lo de los items
#####Pero la misma vaina, probaba el sistema de pelea y necesitaba ver que escogiera
#####Arma, y se pudiera curar y esas vainas. Todavia no he tirado ahi que funcione la
#####pocion de mana, pero porque no he tirado ningun ataque o movimiento magico que
####gaste mana.

class MovAtak:
    def __init__(self):
        raise NotImplementedError("Objeto perteneciente a movimientos creado con vacios")

    def __str__(self):
        if self.damage > 0:
            return "{} ({} Daño Fisico)" .format(self.name, self.damage)
        elif self.magicdamage > 0:
            return "{} ({} Daño Mágico)" .format(self.name, self.magicdamage)


class Nudillo(MovAtak):
    def __init__(self):
        self.name = "Nudillo"
        self.description = "Nudillos de metal para golpe directo"
        self.damage = 25
        self.magicdamage = 0
        self.value = 1


class Daga(MovAtak):
    def __init__(self):
        self.name = "Daga"
        self.description = "Una daga pequeña"
        self.damage = 50
        self.magicdamage = 0
        self.value = 20


class EspadaHierro(MovAtak):
    def __init__(self):
        self.name = "Espada de Hierro"
        self.description = "Una espada básica"
        self.damage = 20
        self.magicdamage = 0
        self.value = 100
        
class Relampago(MovAtak):
    def __init__(self):
        self.name = "Relampago"
        self.description = "Un poderoso hechizo que invoca un relampago que ataca al oponente"
        self.damage = 0
        self.magicdamage = 50
        self.mpcost = 25
        
class Llamarada(MovAtak):
    def __init__(self):
        self.name = "Llamarada"
        self.description = "Un hechizo que hace al oponente incendiarse"
        self.damage = 0
        self.magicdamage = 30
        self.mpcost = 15


class Consumable:
    def __init__(self):
        raise NotImplementedError("Objeto Consumable creado vacio")

    def __str__(self):
        if self.healing_value > 0:
            return "{} (+{} HP)" .format(self.name, self.healing_value)
        elif self.magic_value > 0:
            return "{} (+{} MP)" .format(self.name, self.magic_value)


class LifePotion(Consumable):
    def __init__(self):
        self.name = "Pocion de Vida"
        self.healing_value = 50
        self.magic_value = 0
        self.value = 60

class PanViejo(Consumable):
    def __init__(self):
        self.name = "Pan Viejo"
        self.healing_value = 10
        self.magic_value = 0
        self.value = 60

class BotellaAgua(Consumable):
    def __init__(self):
        self.name = "Botella de Agua"
        self.healing_value = 20
        self.magic_value = 10
        self.value = 60

class MagicPotion(Consumable):
    def __init__(self):
        self.name = "Pocion de Magia"
        self.magic_value = 50
        self.healing_value = 0
        self.value = 60
