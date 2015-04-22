    def hero_attack(self, by = ""):
    if by == "":
       print("Should choose between weapon and spell!")
    else:
        if by == "weapon":

            if  self.__map[self.__hero_pos[0]][self.__hero_pos[1]] == 'E':
                return True
            else:
                return False
        if by == "spell" :

            row_number = self.__get_rows()
            while row_number < 0:
                if self.__map[[row_number][self.__hero_pos[1]]] == 'E':
                    return True
                row_number -= 1

            col_number = self.__get_cols()
            while col_number < 0:
                if self.__map[[self.__hero_pos[0]][col_number]] == 'E':
                    return True
                col_number -= 1


            else:
                return False
