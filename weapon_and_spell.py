
class Weapon:

    def __init__(self, name, damage):
        #self.__name = "no weapon"
        #self.__damage = 0
        self.__name = name
        self.__damage = damage

    def get_damage(self):
        return self.__damage


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.__name = name
        self.__damage = damage
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def get_damage(self):
        return self.__damage

    def get_mana_cost(self):
        return self.__mana_cost

    def get_cast_range(self):
        return self.__cast_range
