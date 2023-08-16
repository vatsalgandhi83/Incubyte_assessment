import unittest
from spacecraft import Spacecraft


class TestSpacecraft(unittest.TestCase):
    def test_move_forward_north(self):
        starting_position = (0, 0, 0)
        initial_direction = "North"
        spacecraft = Spacecraft(*starting_position, initial_direction)
        spacecraft.move_forward()
        self.assertEqual(spacecraft.y, 1)

    def test_move_forward_south(self):
        starting_position = (0, 0, 0)
        initial_direction = "South"
        spacecraft = Spacecraft(*starting_position, initial_direction)
        spacecraft.move_forward()
        self.assertEqual(spacecraft.y, -1)

    def test_move_forward_east(self):
        starting_position = (0, 0, 0)
        initial_direction = "East"
        spacecraft = Spacecraft(*starting_position, initial_direction)
        spacecraft.move_forward()
        self.assertEqual(spacecraft.x, 1)

    def test_move_forward_west(self):
        starting_position = (0, 0, 0)
        initial_direction = "West"
        spacecraft = Spacecraft(*starting_position, initial_direction)
        spacecraft.move_forward()
        self.assertEqual(spacecraft.x, -1)

if __name__ == '__main__':
    unittest.main()
