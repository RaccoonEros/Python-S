import Items


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
                      Items.MagicPotion()]