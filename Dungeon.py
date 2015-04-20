import random
from weapon_and_spell import Weapon, Spell
from Enemy import Enemy
from hero import Hero
class Dungeon:
    def __init__(self, path="", rows=5, cols=8):
       self.__hero = Hero()
       self.__hero_pos = (0,0)
       self.__rows = rows
       self.__cols = cols
       self.__map = []
       self.__last_spawn = (0,0)
       if path != "":
            with open(path) as f:
                lst = f.readlines()
                self.__rows = len(lst)
                self.__cols = len(lst[0])-1
                self.__map = [list(elems[:-1]) for elems in lst]

    def set_map(self, curr_map):
        self.__map = curr_map

    def get_rows(self):
        return self.__rows

    def get_hero(self):
        return self.__hero

    def get_cols(self):
        return self.__cols

    def adj(self, row, col):
        result = []
        if row - 1 >= 0 and self.__map[row - 1][col] == 0:
            result.append((row - 1, col))
        if row + 1 < self.__rows and self.__map[row + 1][col] == 0:
            result.append((row + 1, col))
        if col - 1 >= 0 and self.__map[row][col - 1] == 0:
            result.append((row, col - 1))
        if col + 1 < self.__cols and self.__map[row][col + 1] == 0:
            result.append((row, col + 1))
        return result
    @staticmethod
    def generate_map(rows, cols):
        dungeon = Dungeon(rows=rows, cols=cols)
        #defaulting the self.__map
        dun_rows = dungeon.get_rows()
        dun_cols = dungeon.get_cols()
        curr_map = [[0 for x in range(dun_cols)] for y in range(dun_rows)]
        dungeon.set_map(curr_map)
        #making the road
        lower_end = dun_rows + 2*dun_cols
        upper_end = int(0.6 * dun_rows*dun_cols)
        road_len = random.randint(lower_end, upper_end)
        start_pos = random.choice([(row, col) for row in range(dun_rows) for col in range(dun_cols)])

        #start drawing
        path_to_curr_elem = []
        path_to_curr_elem.append((0,0))
        path_elems = ['.', 'E', '.', 'T', '.', '.']
        row = 0
        col = 0
        to_choose_from = []
        curr_map[row][col] = 'S'
        while road_len >= 0:
            to_choose_from = dungeon.adj(row, col)
            if to_choose_from != []: 
                next_pos = random.choice(to_choose_from)
                row = next_pos[0]
                col = next_pos[1]
                path_to_curr_elem.append((row, col))
                if road_len > 0:
                    curr_map[row][col] = random.choice(path_elems)
                else:
                    curr_map[row][col] = 'G'
                road_len -= 1
                to_choose_from = []
            else:
                curr_map[row][col] = '.'
                dungeon.set_map(curr_map)
                to_choose_from = dungeon.adj(row, col)
                while to_choose_from == []:
                    elem = path_to_curr_elem.pop()
                    dungeon.set_map(curr_map)
                    to_choose_from = dungeon.adj(elem[0], elem[1])
                row = elem[0]
                col = elem[1]
        #adding obsticles(such English, much fail)
        curr_map = [['#' if elem == 0 else elem for elem in row] for row in curr_map]
        dungeon.set_map(curr_map)
        dungeon.spawn(dungeon.get_hero())
        return dungeon

    def print_map(self):
        printable = ""
        for row in range(self.__rows):
            for col in range(self.__cols):
                printable += (self.__map[row][col] + ' ')
            printable += '\n'
        printable = printable[:-1]
        print(printable)

    def spawn(self, hero):
        self.__hero_pos = 'E'
        self.__hero_pos = self.__last_spawn
        self.__hero_pos = (0,0)
        self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = 'H'

    def __movement(self, new_hero_pos):
        if self.__map[new_hero_pos[0]][new_hero_pos[1]] in ['#', 'T', 'E']:
            if self.__map[new_hero_pos[0]][new_hero_pos[1]] == '#':
                return False

            if self.__map[new_hero_pos[0]][new_hero_pos[1]] == 'T':
                self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = '.'
                self.__hero_pos = new_hero_pos

                treasure = self.spawn_treasure()
                if type(treasure) is ManaPotion:
                    print("Mana pot found")
                    mana = treasure.get_mana()
                    self.__hero.take_mana(mana)
                    print("Hero healed with {} mana".format(mana))
                    print("Hero's mana is: {}".format(self.__hero.get_mana()))

                if type(treasure) is HealthPotion:
                    print("Healing pot found!")
                    health = treasure.get_health()
                    self.__hero.take_healing(health)
                    print("Hero healed with {} health".format(health))
                    print("Hero;s health is: {}".format(self.__hero.get_health()))

                if type(treasure) is Weapon:
                    print("Weapon found!")
                    self.__hero.equip(treasure)

                if type(treasure) is Spell:
                    print("Spell found!")
                    self.__hero.learn(treasure)

                self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = 'H'
                return True

            if self.__map[new_hero_pos[0]][new_hero_pos[1]] == 'E':
                print("Enemy found")
                self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = '.'
                self.__hero_pos = new_hero_pos

                #enemy spawner
                enemy = Enemy(health = random.randrange(50,300),
                              mana = random.randrange(20,100),
                              damage = random.randrange(20,200))

                #initiate fight
                #fight = Fight(self.__hero, enemy)
                #fight.start_fight()

                self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = 'H'
        else:
            self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = '.'
            self.__hero_pos = new_hero_pos
            self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = 'H'


    def move_hero(self, direction):
        if direction in ['up', 'down', 'left', 'right']:
            if direction == 'up':
                if self.__hero_pos[0] >= 1:
                    new_hero_pos = (self.__hero_pos[0] - 1,
                                    self.__hero_pos[1])
                    self.__movement(new_hero_pos)
                    self.print_map()
                    return True
                else:
                    return False
            if direction == 'down':
                if self.__hero_pos[0] + 1 <= self.__rows - 1:
                    new_hero_pos = (self.__hero_pos[0] + 1,
                                    self.__hero_pos[1])
                    self.__movement(new_hero_pos)
                    self.print_map()
                    return True
                else:
                    return False
            if direction == 'left':
                if self.__hero_pos[1] >= 1:
                    new_hero_pos = (self.__hero_pos[0],
                                    self.__hero_pos[1] - 1)
                    self.__movement(new_hero_pos)
                    self.print_map()
                    return True
                else:
                    return False

            if direction == 'right':
                if self.__hero_pos[1] + 1 <= self.__cols - 1:
                    new_hero_pos = (self.__hero_pos[0],
                                    self.__hero_pos[1] + 1)
                    self.__movement(new_hero_pos)
                    self.print_map()
                    return True
                else:
                    return False

        else:
            print("Wrong command!!!")

    def spawn_treasure(self):
        weapon_damage = random.randrange(10, 130)
        weap = Weapon("random", weapon_damage)
        spell_damage = random.randrange(5,90)
        spell_cost = random.randrange(2,60)
        spell_range = random.randrange(1, self.__cols - 1)
        spell = Spell("random",spell_damage, spell_cost, spell_range)
        health_potion = HealthPotion()
        mana_potion = ManaPotion()
        to_choose_from = [mana_potion,
                          health_potion,
                          weap,
                          spell]

        return random.choice(to_choose_from)

class ManaPotion:
    def __init__(self):
        self.__health = int(random.randrange(5,90))
    def get_mana(self):
        return int(self.__health)

class HealthPotion:
    def __init__(self):
        self.__health = int(random.randrange(5,150))
    def get_health(self):
        return int(self.__health)


class Fight:
    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy









if __name__ == "__main__":
    #dun = Dungeon.generate_map(rows=12, cols=14)
    #dun.print_map()
    dung = Dungeon.generate_map(7, 14)
