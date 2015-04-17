import random
class Dungeon:
    def __init__(self, path="", rows=5, cols=8):
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
    dun = Dungeon.generate_map(rows=12, cols=14)
    dun.print_map()
