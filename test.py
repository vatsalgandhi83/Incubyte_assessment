import unittest
from spacecraft import Spacecraft # Importing Spacecraft class


class TestSpacecraft(unittest.TestCase):
    def test_move_forward_north(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.move_forward()
        self.assertEqual(spacecraft.y, 1)

TestSpacecraft.test_move_forward_north()
