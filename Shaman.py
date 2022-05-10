# Shaman.py
from random import randint
import string


class Shaman:

    def __init__(self) -> None:
        self .name              = __name__
        self. strong            = string 
        self .weapon_name       = "fists"
        self .weapon_equipped   = None
        self .swing_timer       = 1.5
        self .crit_chance       = 23.5
        self .windfury_chance   = 20.0
        self .crit_multiplier   = 2.0


    def roll(self, chance): # Roll from 0.00-100 and returns if successful
        r =(randint(100,10000)/100) 
        return (r < chance)


    def crit(self):
        return self.roll(self.crit_chance)

    def multiply_damage(self, dmg):
        multiplier = 2 # placeholder for including in the parameters
        return dmg * multiplier

    def windfury(self):
        return self.roll(self.windfury_chance)


    def equip_weapon(self, weapon):
        self .weapon_equipped   = weapon
        self .weapon_name       = weapon.name
        self .swing_timer       = weapon.get_swing_timer()


    def windfury_proc(self, dmg):
        print(f"Windfury! {int(self.weapon_equipped.roll_dmg()*1.2)}")


    def auto_attack(self):
        dmg = self.weapon_equipped.roll_dmg()
        self.multiply_damage(dmg) if self.crit() else print(dmg)



if __name__ == '__main__':
    from Weapon import Weapon

    from json import load

    s = Shaman()
    print(s.name)
    with open('db/lionheart_executioner.json') as json_file:
        sword = load(json_file)

    w = Weapon(sword)
    s.equip_weapon(w)
    s.auto_attack()

