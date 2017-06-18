import unittest

from gol import board


class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.board = board.Board(3, 3)
        self.board.get(0, 0).alive = True
        self.board.get(2, 1).alive = True

    def test_can_reference_cell(self):
        self.board = board.Board(3, 3)
        cell = self.board.get(0, 0)

        self.assertIsInstance(cell, board.Cell)

    def test_cell_equivalence(self):
        cell1 = self.board.get(0, 0)
        cell2 = self.board.get(1, 1)
        cell3 = self.board.get(1, 1)

        self.assertNotEqual(cell1, cell2)
        self.assertEqual(cell2, cell3)

    def test_cell_out_of_bounds_raises(self):
        with self.assertRaises(IndexError):
            self.board.get(100, 100)

    def test_cell_references_neighbors(self):
        cell = self.board.get(1, 1)
        top_left = self.board.get(0, 0)
        top = self.board.get(1, 0)
        top_right = self.board.get(2, 0)
        right = self.board.get(2, 1)
        bottom_right = self.board.get(2, 2)
        bottom = self.board.get(1, 2)
        bottom_left = self.board.get(0, 2)
        left = self.board.get(0, 1)

        self.assertTrue(top_left in cell.neighbors)
        self.assertTrue(top in cell.neighbors)
        self.assertTrue(top_right in cell.neighbors)
        self.assertTrue(right in cell.neighbors)
        self.assertTrue(bottom_right in cell.neighbors)
        self.assertTrue(bottom in cell.neighbors)
        self.assertTrue(bottom_left in cell.neighbors)
        self.assertTrue(left in cell.neighbors)

    def test_edge_cells_wrap_around(self):
        cell = self.board.get(1, 0)
        top_left = self.board.get(0, 2)
        top = self.board.get(1, 2)
        top_right = self.board.get(2, 2)
        right = self.board.get(2, 0)
        bottom_right = self.board.get(2, 1)
        bottom = self.board.get(1, 1)
        bottom_left = self.board.get(0, 1)
        left = self.board.get(0, 0)

        self.assertTrue(top_left in cell.neighbors)
        self.assertTrue(top in cell.neighbors)
        self.assertTrue(top_right in cell.neighbors)
        self.assertTrue(right in cell.neighbors)
        self.assertTrue(bottom_right in cell.neighbors)
        self.assertTrue(bottom in cell.neighbors)
        self.assertTrue(bottom_left in cell.neighbors)
        self.assertTrue(left in cell.neighbors)

    def test_corner_cells_wrap_around(self):
        cell = self.board.get(0, 0)
        top_left = self.board.get(2, 2)
        top = self.board.get(0, 2)
        top_right = self.board.get(1, 2)
        right = self.board.get(1, 0)
        bottom_right = self.board.get(1, 1)
        bottom = self.board.get(0, 1)
        bottom_left = self.board.get(2, 1)
        left = self.board.get(2, 0)

        self.assertTrue(top_left in cell.neighbors)
        self.assertTrue(top in cell.neighbors)
        self.assertTrue(top_right in cell.neighbors)
        self.assertTrue(right in cell.neighbors)
        self.assertTrue(bottom_right in cell.neighbors)
        self.assertTrue(bottom in cell.neighbors)
        self.assertTrue(bottom_left in cell.neighbors)
        self.assertTrue(left in cell.neighbors)

    def test_cell_can_count_neighboring_alive(self):
        cell = self.board.get(1, 1)
        self.assertEqual(2, cell.neighbors_alive)

    def test_cell_can_count_neighbording_dead(self):
        cell = self.board.get(1, 1)
        self.assertEqual(6, cell.neighbors_dead)


if __name__ == '__main__':
    unittest.main()
