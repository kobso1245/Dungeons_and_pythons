
class Hero:
    def __init__ (self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.start_health=100
        self.health = health
        self.start_mana=100
        self.mana = mana
        self.mana_regeneration_rate = 2

    def known_as(self):
        return "{} the {}".format(self.get_name(), self.get_title())

    def get_name(self):
        return self.name

    def get_title ( self):
        return self.title

    def get_health(self):
        return self.health

    def get_mana (self):
        return self.mana

    def is_alive(self):
        if get_heath(self)>0:
            return True
        return False







