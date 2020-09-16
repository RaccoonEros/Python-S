import Monster
import random
import sys
import time
import NPC

###################Definicion de la clase base para el mundo en que se situa el juego####
##############O lo que llamamos los tiles o mapas ##################################
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def init_text(self):
        raise NotImplementedError("Error, la introduccion no pudo cargar")

    def intro_text(self):
        raise NotImplementedError("El texto no esta disponible")

    def modify_player(self, player):
        pass

#########################Introducción del Juego##############################
class Posic(MapTile):
    def PosIni(self):
        self.ubicacion_personaje_x=1.5
        self.ubicacion_personaje_y=0.5


class StartTile(MapTile):
    def init_text(self):
            IntroGame = "Mientras investigaba un antiguo calabozo en busca de un tesoro antiguo, \nen la ultima habitacion donde reside la tumba de un antiguo nigromante \nuna trampa fue activada al reconocer un intruso en el area. \n \nEsto ha cerrado su ruta de retorno y ha activado a los monstruos de la \nzona, no queda mas opcion que luchar contra ellos y deshabilitar el mecanismo \nque lo ha encerrado. Quien sabe, tal vez el tesoro se encuentre aqui tambien."
            for char in IntroGame:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
            return "\n"
    def intro_text(self):
        text = "Sala de Inicio \n"
        return text
    
class EmptyTile(MapTile):
    def intro_text(self):
        text = "Casilla en blanco, descansa un poco"
        return text


#Condiciones para la aparición aleatoria de los monstruos y el texto de aparicion y muerte#
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.20:
            self.Monster = Monster.Rat()
            self.alive_text = "Una Rata salvaje te amenaza \n"
            self.dead_text = "Mataste la Rata\n"
        elif r < 0.40:
            self.Monster = Monster.Bat()
            self.alive_text = "Un Murcielago vuela cerca de ti\n"
            self.dead_text = "El murcielago ha caido\n"
        elif r < 0.50:
            self.Monster = Monster.Goblin()
            self.alive_text = "Escuchas risas siniestras... un Goblin aparece frente a ti\n" 
            self.dead_text = "El cuerpo del goblin yace en el suelo\n"
        elif r < 0.60:
            self.Monster = Monster.Ogre()
            self.alive_text = "Mientras escuchas pasos golpear fuertemente el suelo" \
                              "... de repente, un Ogro aparece\n"
            self.dead_text = "Con un fuerte sonido al caer, el Ogro ha muerto\n"
        elif r < 0.70:
            self.Monster = Monster.SkeletonS()
            self.alive_text = "La habitación comienza a sentirse mas fria" \
                              "... y sin hacer mas ruido que un \ntic tac molesto" \
                              "un Esqueleto armado con \nuna espada esta frente a ti"
            self.dead_text = "Escuchas los golpes que dan los huesos al gopearse"\
                             " mientras el esqueleto sucumbe ante ti\n"
        elif r < 0.80:
            self.Monster = Monster.SkeletonL()
            self.alive_text = "La habitación comienza a sentirse mas fria" \
                              "... y sin hacer mas ruido que un\ntic tac molesto" \
                              "un Esqueleto armado con\nuna lanza esta frente a ti"
            self.dead_text = "Escuchas los golpes que dan los huesos al gopearse"\
                             " mientras el esqueleto sucumbe ante ti\n"        
        elif r < 0.90:
            self.Monster = Monster.Ghost()
            self.alive_text = "Sientes una presencia, pero no puedes ubicarla" \
                              "...de repente, una sombra comienza\na formarse en el aire"\
                              " y frente a ti, la silueta de un fantasma aparece!!!"
            self.dead_text = "Escuchas un chillido de lamento mientras se desintegra el fantasma\n"
        else:
            self.Monster = Monster.FireSpirit()
            self.alive_text = "Te detienes de repente, no lo puedes creer, una columna" \
                              " de fuego se ha formado!\ny de la misma emerge una silueta"\
                              " con una figura que parece una especie de \nespiritu con forma"\
                              "de humanoide"
            self.dead_text = "Mientras retrocede, vez como el espiritu de fuego colapsa sobre" \
                             " si mismo y se \nreduce a una pequeña columna de humo que se disipa\n"

        super().__init__(x, y)
#####################Condicional de introduccion de texto de cada monstruo#################
    def intro_text(self):
        if self.Monster.hp == 100:
            text = self.alive_text
        elif self.Monster.hp <= 0:
            text = self.dead_text
        else :
            text = ''
        return text

##########################Condiciones del sistema de pelea entre PJ y Monstruos##########
    def modify_player(self, player):
        rr = random.random()
        if self.Monster.still_alive():
            if rr < 0.45:
                try:
                    player.hp = player.hp - (self.Monster.daño1/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk1, (self.Monster.daño1/player.defense), player.hp))
                except:
                    rr = random.random()
            elif rr < 0.75:
                try:
                    player.hp = player.hp - (self.Monster.daño2/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk2, (self.Monster.daño2/player.defense), player.hp))
                except:
                    rr = random.random()
            else :
                try:
                    player.hp = player.hp - (self.Monster.daño3/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk3, (self.Monster.daño3/player.defense), player.hp))
                except:
                    rr=random.random()


############################Enfrentamiento Subjefe####################                    
class SubBossTile(MapTile):
    def __init__(self, x, y):
        self.Monster = Monster.Acolito()
        self.alive_text = "Te has topado con un subjefe, uno de los aprendices del Nigromante"
        self.dead_text = "Ha sido un combate duro, pero finalmente, el adepto oscuro ha caido"
        super().__init__(x, y)

    def intro_text(self):
        if self.Monster.hp == 100:
            text = self.alive_text
        elif self.Monster.hp <= 0:
            text = self.dead_text
        else :
            text = ''
        return text

    def modify_player(self, player):
        rr = random.random()
        if self.Monster.still_alive():
            if rr < 0.45:
                try:
                    player.hp = player.hp - (self.Monster.daño1/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk1, (self.Monster.daño1/player.magicdefense), player.hp))
                except:
                    rr = random.random()
            elif rr < 0.75:
                try:
                    player.hp = player.hp - (self.Monster.daño2/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk2, (self.Monster.daño2/player.magicdefense), player.hp))
                except:
                    rr = random.random()
            else :
                try:
                    player.hp = player.hp - (self.Monster.daño3/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk3, (self.Monster.daño3/player.magicdefense), player.hp))
                except:
                    rr=random.random()

                    
                    
############################Enfrentamiento Jefe Final####################                    
class BossTile(MapTile):
    def __init__(self, x, y):
        self.Monster = Monster.Nigromante()
        self.alive_text = "Divisas una tumba en el centro de la mazmora... pero esta comienza a \nmoverse automaticamente, no lo puedes creer, el nigromanten o esta muerto \nusando algun oscuro hechizo, se ha convertido en un Licht muy poderoso"
        self.dead_text = "Tras vencer al Nigromante que aguardaba en esta mazmorra, observas \nun camino iluminarse detras de ti, es la salida de la mazmorra"
        super().__init__(x, y)

    def intro_text(self):
        if self.Monster.hp == 100:
            text = self.alive_text
        elif self.Monster.hp <= 0:
            text = self.dead_text
        else :
            text = ''
        return text

    def modify_player(self, player):
        rr = random.random()
        if self.Monster.still_alive():
            if rr < 0.45:
                try:
                    player.hp = player.hp - (self.Monster.daño1/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk1, (self.Monster.daño1/player.magicdefense), player.hp))
                except:
                    rr = random.random()
            elif rr < 0.75:
                try:
                    player.hp = player.hp - (self.Monster.daño2/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk2, (self.Monster.daño2/player.magicdefense), player.hp))
                except:
                    rr = random.random()
            else :
                try:
                    player.hp = player.hp - (self.Monster.daño3/player.defense)
                    print("{} uso {} y te hizo {} puntos de daño. Te quedan {} HP.\n".
                        format(self.Monster.name, self.Monster.atk3, (self.Monster.daño3/player.magicdefense), player.hp))
                except:
                    rr=random.random()
        

###################################Condición de Victoria ###############################
class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        Una vez muerto el nigromante, das un suspiro
        por lo cansado de tu aventura, y sigues el 
        sendero que se ha iluminado al caer el nigromante


        Esta primer aventura ha concluido, VICTORIA!
        """

#############################Encontrar oro en el mapa###################################
class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} oro adquirido.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            text = "Ya has tomado el oro que estaba en esta habitación"
            return text
        else:
            text = "Encontraste algunas piezas de oro"
            return text

#############################Codigo para NPC y la tienda ##############################
class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = NPC.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Escoja la acción que desea (C)omprar, (V)ender, or (S)alir?")
            user_input = input()
            if user_input in ['S', 's']:
                return
            elif user_input in ['C', 'c']:
                print("Items disponibles: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['V', 'v']:
                print("Items que puedes vender: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Opcion inválida")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Escoja un item o presione Q para salir: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Opcion invalida")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("Es demasiado caro")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trato completado")

    def intro_text(self):
        text = "Un ser extraño, definitivamente no humano, se encuentra en\n la habitación, muestra un bolso de monedas y te invita \n a ver, parece dispuesto a trancear"
        return 
######################Mapa de la mazmorra, a sustituir por el codigo de Chiza#############
### Ademas lo saque de la web para probar el sistema de pelea y no le entiendo un carajo###
world_dsl = """
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |FG|FG|FG|FG|  |  |ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|SB|FG|FG|  |  |
|  |  |FG|TT|FG|FG|  |  |EN|  |  |  |  |  |  |  |  |  |  |  |FG|FG|FG|  |  |
|  |  |FG|FG|FG|FG|  |  |EN|  |  |ET|ET|ET|ET|EN|ET|EN|EN|  |FG|FG|TT|  |  |
|  |  |  |  |SB|  |  |  |EN|  |  |EN|  |  |  |ET|  |  |EN|  |  |  |  |  |  |
|  |  |  |  |EN|EN|EN|EN|EN|  |  |ET|  |  |ET|EN|ET|  |EN|EN|EN|EN|EN|  |  |
|  |  |  |  |EN|  |  |  |EN|  |  |ET|  |  |ET|EN|ET|  |EN|  |  |  |EN|  |  |
|  |  |  |  |EN|  |  |  |EN|  |  |ET|  |  |  |EN|  |  |EN|  |  |EN|EN|EN|  |
|  |  |  |  |EN|  |EN|EN|ET|EN|ET|EN|  |EN|EN|EN|EN|  |EN|EN|  |EN|EN|EN|  |
|  |  |  |  |EN|  |EN|  |EN|  |  |  |  |EN|  |  |EN|  |  |EN|  |  |  |  |  |
|  |  |  |  |EN|EN|EN|  |ET|  |  |EN|EN|EN|  |EN|EN|EN|  |EN|  |  |  |  |  |
|  |  |  |  |  |  |  |  |EN|  |  |ET|  |  |  |EN|FB|EN|  |EN|EN|EN|EN|EN|  |
|  |  |  |ET|ET|FG|ET|ET|ET|  |  |EN|  |  |  |  |VT|  |  |  |EN|  |  |  |  |
|  |  |  |FG|ET|EN|ET|ET|ET|  |  |ET|  |  |  |  |  |  |  |  |EN|  |EN|EN|  |
|  |  |  |ET|ET|ET|FG|ET|ET|  |  |EN|ET|ET|EN|  |ET|EN|ET|ET|EN|EN|EN|EN|  |
|  |  |  |EN|  |  |  |  |  |  |  |  |  |  |ET|  |ET|  |  |ET|  |  |EN|EN|  |
|  |EN|ET|EN|  |  |  |  |  |  |  |  |  |  |ET|  |EN|  |  |ET|  |  |  |  |  |
|  |ET|  |  |  |  |  |  |  |  |  |  |  |  |EN|EN|EN|  |  |ET|  |FG|FG|FG|  |
|  |EN|  |  |  |FG|FG|FG|  |  |  |  |  |  |  |SB|  |  |  |ET|  |FG|TT|EN|  |
|  |ET|  |  |  |FG|FG|FG|  |  |  |  |  |  |FG|FG|FG|  |EN|ET|  |FG|FG|FG|  |
|  |ET|  |  |  |  |SB|  |  |  |  |  |  |  |FG|TT|FG|  |  |ET|  |  |SB|  |  |
|  |EN|ET|EN|  |  |ET|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |ET|  |  |
|  |  |  |ET|  |  |ET|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |ET|  |  |
|  |  |  |EN|  |  |EN|  |  |  |EN|EN|  |  |  |  |  |EN|ET|  |  |  |EN|  |  |
|  |EN|ET|EN|ET|ET|ET|ET|ET|ET|EN|EN|ET|ET|ET|ET|EN|EN|ET|ET|ET|ET|EN|  |  |
|  |EN|  |  |  |  |  |  |  |  |EN|EN|  |  |  |  |  |EN|ET|  |  |  |  |  |  |
|  |ST|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ET": EmptyTile,
                  "SB": SubBossTile,
                  "FB": BossTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "  ": None}


world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("Cagada")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
    
