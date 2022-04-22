class TargetDummy:
    def __init__(self, hp, armor) -> None:
        self.hp = hp
        self.armor = armor
        self.alive = True

    def set_dead(self):
        print(f"{__name__} dies* (Overkill: {self.hp})")
        self.hp = 1
        self.alive = False

    def taken_dmg(self, dmg):
        print(f"{__name__} takes {dmg} damage")
        if self.hp <= dmg:
            self.set_dead()
        else:
            self.set_HP(self.hp - dmg)
        

    def set_HP(self, new_hp):
        self.hp = new_hp
        

if __name__ == '__main__':
    td1 = TargetDummy(1000, 20)
    print(td1.hp)