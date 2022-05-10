from random import randint
class Shaman:

    def __init__(self) -> None:
        self .name              = __name__
        self .weapon_name       = "fists"
        self .weapon_equipped   = None
        self .swing_timer       = 1.5
        self .crit_chance       = 23.5
        self .windfury_chance   = 20.0

    def crit(self, dmg):
        r =(randint(100,10000)/100)
        if r < self.crit_chance:
            return dmg*2
        return dmg

    def equip_weapon(self, weapon):
        self .weapon_equipped   = weapon
        self .weapon_name       = weapon.name
        self .swing_timer       = weapon.get_swing_timer()

    def windfury_proc(self, dmg):
        print(f"Windfury! {self.weapon_equipped.roll_dmg()*1.2}")

    def swing_weapon(self):
        print(self .weapon_equipped.name)
        r =(randint(100,10000)/100)
        wf =(randint(100,10000)/100)

        print(r)
        if r < self.crit_chance:
            print(f"Critical hit {self.weapon_equipped.roll_dmg() *2}")
            self.windfury_proc(wf)
        else:
            print(self .weapon_equipped.roll_dmg())
            self.windfury_proc(wf)



if __name__ == '__main__':
    from Weapon import Weapon

    from json import load

    s = Shaman()
    print(s.name)
    with open('db/lionheart_executioner.json') as json_file:
        sword = load(json_file)

    w = Weapon(sword)
    s.equip_weapon(w)
    s.swing_weapon()

