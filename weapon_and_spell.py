
class Weapon:

    def __init__( self, name, damage):
        self.__name = "no weapon"
        self.__damage = 0

    def get_damage( self):
        return self.__damage



class Spell:

    def __init__( self, name, damage, mana_cost, cast_range):
        self.__name = name
        self.__damage = 20
        self.__mana_cost = 30
        self.__cast_range = 1

    def get_damage( self):
        return self.__damage

    def get_mana_cost( self):
        return self.__mana_cost

    def get_cast_range( self):
        return self.__cast_range
