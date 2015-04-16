
class Hero:
    def __init__ ( self, name, title, health, mana, mana_regeneration_rate):
        self.__name = name
        self.__title = title
        self.__start_health = 100
        self.__health = health
        self.__start_mana = 100
        self.__mana = mana
        self.__mana_regeneration_rate = 2


    def known_as( self):

        return "{} the {}".format(self.get_name(), self.get_title())


    def get_name( self):

        return self.__name


    def get_title ( self):

        return self.__title


    def get_health( self):

        return self.__health


    def get_mana ( self):

        return self.__mana


    def is_alive( self):

        if get_health( self) > 0:
            return True
        return False


    def can_cast( self):

        if get_mana( self) > 0:
            return True
        return False


    def take_damage( self, damage_points):

        if self.__health < damage_points:
            self.__health = 0
        else:
            self.__health = self.__health - damage_points


    def take_healing( self, healing_points):
        if is_alive(self) == False
            return False

        a = self.__health + healing_points

        if a > self.__start_health:
            self.__health = self.__start_health
        else:
            self.__health = a

        return True


    def take_mana( self, mana_points):
        a = self.__mana + mana_points

        if a > self.__start_mana:
            self.__mana = self.__start_mana
        else:
            self.__mana = a


    def equip(self, weapon):
        pass








