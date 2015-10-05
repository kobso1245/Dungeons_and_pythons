class Enemy:

    def __init__(self, health=100, mana=100, damage=20):
        self.__health = health
        self.__start_health = health
        self.__start_mana = mana
        self.__mana = mana
        self.__damage = damage
        self.__weapon = 0
        self.__spell = 0

    def is_alive(self):
        if self.__health:
            return True
        else:
            return False

    def can_cast(self):
        pass

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def get_damage(self):
        return self.__damage

    def take_mana(self, mana_points):
        if self.__mana + mana_points > self.__start_mana:
            self.__mana = self.__start_mana
        else:
            self.__mana += mana_points

    def take_healing(self, healing_points):
        if self.__health <= 0:
            return False
        else:
            if self.__heallth + healing_points > self.__start_health:
                self.__health = self.__start_health
            else:
                self.__health += healing_points
        return True

    def equip(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapon = weapon
            return
        else:
            print("Wrong weapon")
            return False

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.__spell = spell
            return
        else:
            print("Wrong input")
            return False

    def atack(self):
        return self.get_damage()

    def take_damage(self, damage):
        if self.__health - damage <= 0:
            self.__health = 0
        else:
            self.__health -= damage
