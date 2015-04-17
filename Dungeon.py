import random
class Dungeon:
    def __init__(self, path, rows=5, cols=8):
       self.__hero_pos = (0,0)
       self.__rows = rows
       self.__cols = cols
       self.__map = []
       self.__last_spawn = (0,0)
       with open(path) as f:
           lst = f.readlines()
           self.__rows = len(lst)
           self.__cols = len(lst[0])-1
           self.__map = [list(elems[:-1]) for elems in lst]

    def print_map(self):
        printable = ""
        for row in range(self.__rows):
            for col in range(self.__cols):
                printable += self.__map[row][col]
            printable += '\n'
        printable = printable[:-1]
        print(printable)

    def spawn(self, hero):
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__map[row][col] == 'S':
                    self.__map[row][col] = 'H'
                    return
        self.__map[0][0] = 'H'

    def __movement(self, new_hero_pos):
        if self.__map[new_hero_pos[0]][new_hero_pos[1]] in ['#', 'T', 'E']:
            if self.__map[new_hero_pos[0]][new_hero_pos[1]] == '#':
                return False

            if self.__map[new_hero_pos[0]][new_hero_pos[1]] == 'T':
                print("Treasure found: ")
                self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = '.'
                self.__hero_pos = new_hero_pos
                self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = 'H'
                return True

            if self.__map[new_hero_pos[0]][new_hero_pos[1]] == 'E':
                print("Enemy found")
                self.__map[self.__hero_pos[0]][self.__hero_pos[1]] = '.'
                self.__hero_pos = new_hero_pos
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
                    return True
                else:
                    return False
            if direction == 'down':
                if self.__hero_pos[0] + 1 <= self.__rows - 1:
                    new_hero_pos = (self.__hero_pos[0] + 1,
                                    self.__hero_pos[1])
                    self.__movement(new_hero_pos)
                    return True
                else:
                    return False
            if direction == 'left':
                if self.__hero_pos[1] >= 1:
                    new_hero_pos = (self.__hero_pos[0],
                                    self.__hero_pos[1] - 1)
                    self.__movement(new_hero_pos)
                    return True
                else:
                    return False

            if direction == 'right':
                if self.__hero_pos[1] + 1 <= self.__cols - 1:
                    new_hero_pos = (self.__hero_pos[0],
                                    self.__hero_pos[1] + 1)
                    self.__movement(new_hero_pos)
                    return True
                else:
                    return False

        else:
            print("Wrong command!!!")

if __name__ == "__main__":
    dun = Dungeon("tst_map")
    dun.print_map()
    dun.spawn("da")
    dun.print_map()
    print()
    print(dun.move_hero("left"))
    dun.print_map()
    print()
    print(dun.move_hero("right"))
    dun.print_map()
    print()
    print(dun.move_hero("up"))
    dun.print_map()
    print()
    print(dun.move_hero("down"))
    dun.print_map()
