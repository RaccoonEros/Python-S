import Items

######Hiiiiper basico, solamente porque un alero estaba jugando el RE4 y que me pije llega
######ver a ese kbron decir "Stranger, stranger" jajajaja, totalmente opcional, podemos
######quitarlo si queremos, ya es opinion de ustedes.

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Objeto NPC creado vacio")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [Items.LifePotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion(),
                      Items.LifePotion(),
                      Items.LifePotion(),
                      Items.MagicPotion(),
                      Items.MagicPotion()]