#Creacion del Bestiario: Nombres y Características de los Monstruos
#Todavia me falta ver que onda con la resistencia magica y cuanta exp den al morir
class Monster:
    def __init__(self):
        raise NotImplementedError("Error en creación de monstruo")
    
    def __str__(self):
        return self.name

    def still_alive(self):
        return self.hp > 0

class Goblin(Monster):
    def __init__(self):
        self.name = "Goblin"
        self.hp = 100
        self.defense = 2
        self.mp = 15
        self.spd = 3
        self.exp = 25
        self.atk1 = "Daga Env"
        self.atk2 = "Pedrada"
        self.daño1 = 6
        self.daño2 = 4

class Ogre(Monster):
    def __init__(self):
        self.name = "Ogro"
        self.hp = 100
        self.defense = 4
        self.mp = 0
        self.spd = 2
        self.exp = 30
        self.atk1 = "Puñetazo"
        self.atk2 = "Embestida"
        self.daño1 = 8
        self.daño2 = 10

class SkeletonS(Monster):
    def __init__(self):
        self.name = "EsqueletoS"
        self.hp = 100
        self.defense = 4
        self.mp = 0
        self.spd = 3
        self.exp = 30
        self.atk1 = "Espada"
        self.daño1 = 12

class SkeletonL(Monster):
    def __init__(self):
        self.name = "EsqueletoL"
        self.hp = 100
        self.defense = 4
        self.mp = 0
        self.spd = 3
        self.exp = 30
        self.atk1 = "Lanza" 
        self.daño1 = 14
 
class Rat(Monster):
    def __init__(self):
        self.name = "Rata"
        self.hp = 100
        self.defense = 0
        self.mp = 0
        self.spd = 3
        self.exp = 10
        self.atk1 = "Arañazo"
        self.atk2 = "Mordisco"
        self.daño1 = 5 
        self.daño2 = 6

class Bat(Monster):
    def __init__(self):
        self.name = "Murcielago"
        self.hp = 100
        self.defense = 0
        self.mp = 0
        self.spd = 3
        self.exp = 10
        self.atk1 = "Arañazo"
        self.atk2 = "Mordisco"
        self.atk3 = "Aullido"
        self.daño1 = 5
        self.daño2 = 6
        self.daño3 = 5

class Ghost(Monster):
    def __init__(self):
        self.name = "Fantasma"
        self.hp = 100
        self.defense = 3
        self.mp = 40
        self.spd = 3
        self.exp = 25
        self.atk1 = "Lamento"
        self.atk2 = "Maldición"
        self.atk3 = "Drena"
        self.daño1 = 7
        self.daño2 = 10
        self.daño3 = 8

class FireSpirit(Monster):
    def __init__(self):
        self.name = "Espiritu de Fuego"
        self.hp = 100
        self.defense = 3
        self.mp = 60
        self.spd = 5
        self.exp = 50
        self.atk1 = "Asqua"
        self.atk2 = "Bola de Fuego"
        self.atk3 = "Llamarada"
        self.daño1 = 10
        self.daño2 = 15
        self.daño3 = 17

########Aca este lo tengo pensado tirar como subjefe
class Acolito(Monster):
    def __init__(self):
        self.name = "Acólito Óscuro"
        self.hp = 100
        self.defense = 4
        self.mp = 130
        self.spd = 5
        self.exp = 100
        self.atk1 = "Ola de Frio"
        self.atk2 = "Oscuridad"
        self.atk3 = "Báculo"
        self.daño1 = 30
        self.daño2 = 40
        self.daño3 = 10


##########Y este kbron sera el final boss
class Nigromante(Monster):
    def __init__(self):
        self.name = "Nigromante"
        self.hp = 100
        self.defense = 5
        self.mp = 200
        self.spd = 7
        self.exp = 300
        self.atk1 = "Nosferatu"
        self.atk2 = "Toque Maldito"
        self.atk3 = "Relámpago"
        self.daño1 = 60
        self.daño2 = 20
        self.daño3 = 85