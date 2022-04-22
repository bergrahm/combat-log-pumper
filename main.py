from Shaman import Shaman
from TargetDummy import TargetDummy
from Weapon import Weapon
from time import sleep
from json import load

with open('db/lionheart_executioner.json') as json_file:
    sword = load(json_file)

shammy = Shaman()
print(f"Weapon Equiped:{shammy.weapon_name}")

w1 = Weapon(sword)
td1 = TargetDummy(10000, 0)
shammy.equip_weapon(w1)
print(f"Weapon Equiped: {shammy.weapon_name}")

while td1.alive:
    td1.taken_dmg(w1.roll_dmg())
    sleep(shammy.swing_timer)