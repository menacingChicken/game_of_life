class Engine(object):
    def __init__(self, board):
        self._board = board

    def step(self):
        board_snapshot = self.make_snapshot()

        for snapshot_cell, current_cell in zip(board_snapshot, self._board):
            if snapshot_cell.is_alive and snapshot_cell.neighbors_alive not in [2, 3]:
                current_cell.alive = False

            elif snapshot_cell.is_dead and snapshot_cell.neighbors_alive == 3:
                current_cell.alive = True

    def make_snapshot(self):
        from board import Board

        board = Board(self._board.width, self._board.height)

        for cell in self._board:
            board.get(cell.pos.x, cell.pos.y).alive = cell.alive

        return board
