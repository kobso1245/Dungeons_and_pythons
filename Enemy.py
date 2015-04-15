class Enemy():
    def __init__(self, health=100, mana=100, damage=20):
        self.__health = health
        self.__start_health = health
        self.__start_mana = mana
        self.__mana = mana
        self.__damage = damage
        self.__weapon = 0
        self.__spell = 0

    def is_alive(self):
        if healt:
            return True
        else:
            return False

    def can_cast(self):
        pass

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def take_mana(self, mana_points):
        if self.__mana + mana_points > self.__start_mana:
            self.__mana = self.__start_mana
        else:
            self.__mana += mana_points

    def take_healing(self, healing_points):
        if self.__health <=0:
            return False
        else:
            if self.__heallth + healing_points > self.__start_health:
                self.__health = self.__start_health
            else:
                self.__health += healing_points
        return True

    def equip(self, weapon):
        if type(weapon) is Weapon:
            self.__weapon = weapon
            return
        if type(weapon) is Spell:
            self.__spell = weapon
            return
        else:
            print("Wrong weapon")
            return False

    def attack(self, by=""):
        if by == "":
            return self.__damage
        else:
            if by == "weapon" and self.__weapon != 0:
                return self.__weapon.get_damage()
            if by == "weapon" and self.__weapon == 0:
                print("No weapon equipped!!")
                return False
            if by == "spell" and self.__spell != 0:
                if self.__mana >= self.__spell.get_mana_cost():
                    self.__mana -= self.__spell.get_mana_cost()
                    return self.__spell.get_damage()
                else:
                    return False

            if by == "spell" and self.__spell == 0:
                print("No spell found!")
                return False

