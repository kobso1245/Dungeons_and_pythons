from Dungeon import Dungeon
from hero import Hero


def main():
    inp = input(
        "Please write how many rows and how many columns you want in the format: rows cols ").split(' ')
    dung = Dungeon.generate_map(int(inp[0]), int(inp[1]))

    while True:
        direction = input(
            "Please write down a direction (up, down, left, right) or 'fight' to kill the closest enemy: ")
        if not dung.move_hero(direction):
            print("Cannot move that way!")


main()
