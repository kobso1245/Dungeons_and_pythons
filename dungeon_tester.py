import unittest
from Dungeon import Dungeon


class DungeonTest(unittest.TestCase):

    def setUp(self):
        self.dungeon = Dungeon("test", 5, 10)

    def test_movement(self):
        self.assertFalse(self.dungeon.move_hero(('up')))

    def test_movement_down(self):
        self.assertTrue(self.dungeon.move_hero(('down')))

    def test_movement_left(self):
        self.assertFalse(self.dungeon.move_hero(('left')))

    def test_movement_right(self):
        self.assertTrue(self.dungeon.move_hero(('right')))

    def test_movement_lower_right_corner(self):
        self.dungeon._Dungeon__hero_pos = (4, 9)
        self.assertFalse(self.dungeon.move_hero(('down')))
        self.assertFalse(self.dungeon.move_hero(('right')))
        self.assertTrue(self.dungeon.move_hero(('up')))
        self.assertTrue(self.dungeon.move_hero(('left')))


if __name__ == "__main__":
    unittest.main()
