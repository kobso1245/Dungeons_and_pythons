class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def static_fight(self):
        enemy_health = 1
        hero_health = 1

        if not self.enemy.get_health():
            return True
        if not self.hero.get_health():
            return False

        while enemy_health and hero_health:
            self.enemy.take_damage(self.hero.atack())
            enemy_health = self.enemy.get_health()
            if not enemy_health:
                return True
            self.hero.take_damage(self.hero.atack())
            hero_health = self.hero.get_health()
            if not hero_health:
                return False

    def moving_fight(self):
        if self.enemy.get_health():
            self.enemy.take_damage(self.hero.atack())
        else:
            return True
