from random import randint

class Weapon:
    def __init__(self, blueprint: dict) -> None:
        self .name          = blueprint["name"]
        self .min_DMG       = blueprint["min_dmg"]
        self .max_DMG       = blueprint["max_dmg"]
        self .swing_timer   = blueprint["swing_timer"]


    def getMin(self):
        return self.min_DMG


    def getMax(self):
        return self.max_DMG


    def get_swing_timer(self):
        return self.swing_timer


    def roll_dmg(self):
        return randint(self.min_DMG, self.max_DMG)

# Testing
if __name__ == '__main__':
    from json import load

    with open('db/lionheart_executioner.json') as json_file:
        sword = load(json_file)

    shrekFist = Weapon(sword)
    print(shrekFist.getMin())
    print(shrekFist.getMax())
    print(shrekFist.get_swing_timer())
    #shrekFist.getMin()