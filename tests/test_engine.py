import unittest

from gol import engine
from gol import board


class EngineTestCase(unittest.TestCase):
    def setUp(self):
        self.board = board.Board(5, 5)
        self.engine = engine.Engine(self.board)

        self.board.get(1, 1).alive = True
        self.board.get(2, 2).alive = True
        self.board.get(1, 3).alive = True
        self.board.get(0, 4).alive = True
        self.board.get(1, 4).alive = True
        self.board.get(0, 3).alive = True

    def test_any_live_cell_with_fewer_than_2_live_neighbors_dies(self):
        self.engine.step()
        self.assertFalse(self.board.get(1, 1).is_alive)

    def test_any_live_cell_with_2_or_3_live_neighbors_lives(self):
        self.engine.step()
        self.assertTrue(self.board.get(2, 2).is_alive)

    def test_any_live_cell_with_greater_than_3_neighors_dies(self):
        self.engine.step()
        self.assertFalse(self.board.get(1, 3).is_alive)

    def test_any_dead_cell_with_3_neighbors_becomes_alive(self):
        self.engine.step()
        self.assertTrue(self.board.get(1, 0).is_alive)
