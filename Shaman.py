class Shaman:

    def __init__(self) -> None:
        self .name          = __name__
        self .weapon_name   = "fists"
        self .swing_timer   = 1.5
        self .crit_chance   = 23.0

    def equip_weapon(self, weapon):
        self .weapon_name   = weapon.name
        self .swing_timer   = weapon.get_swing_timer()


if __name__ == '__main__':
    s = Shaman()
    print(s.name)