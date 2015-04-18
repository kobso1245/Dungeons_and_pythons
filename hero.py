
class Hero:
    def __init__ ( self, name, title, health, mana, mana_regeneration_rate):
        self.__name = name
        self.__title = "Bron"
        self.__start_health = 100
        self.__health = health
        self.__start_mana = 100
        self.__mana = mana
        self.__mana_regeneration_rate = 2
        self.__weapon = weapon
        self.__spell = spell


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

    def get_mana_regeneration_rate(self):
        return self.__mana_regeneration_rate


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
        if is_alive(self) == False:
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
        if type(weapon) is Weapon:
            self.__weapon = weapon
        else:
            print("This is not a weapon")
            return False


    def learn(self, spell):
        if type(spell) is Spell:
            self.__spell = spell
        else:
            print("This is not a spell")
            return False

    def attack(self, by= ""):
        if by == "weapon" :
            return self.__weapon.get_damage()
        if by == "spell":
            if self.__mana >= self.__spell.get_mana_cost():
                self.__mana -= self.__spell.get_mana_cost()
                return self.__spell.get_damage()
            else:
                return False
















