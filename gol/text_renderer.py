import time

from engine import Engine
from board import Board


board = Board(10, 10)


class TextGameOfLife(object):
    def __init__(self):
        self._width = 10
        self._height = 10
        self._board = Board(self._width, self._height)
        self._engine = Engine(self._board)

    def init_game_board(self):
        self._board.get(1, 1).alive = True
        self._board.get(2, 2).alive = True
        self._board.get(1, 3).alive = True
        self._board.get(0, 4).alive = True
        self._board.get(1, 4).alive = True
        self._board.get(0, 3).alive = True

        #glider
        self._board.get(6, 6).alive = True
        self._board.get(7, 7).alive = True
        self._board.get(7, 8).alive = True
        self._board.get(6, 8).alive = True
        self._board.get(5, 8).alive = True

    def main_loop(self):
        self.init_game_board()
        index = 0
        while True:
            self._render_board()
            print "Step %i complete" % index
            self._wait()

            self._engine.step()
            index += 1

    def _wait(self):
        raw_input()

    def _render_board(self):
        for y in range(self._height):
            for x in range(self._width):
                if self._board.get(x, y).is_alive:
                    print ".",
                else:
                    print " ",
            print


class ContinuatingLoop(TextGameOfLife):
    def __init__(self, delay):
        super(ContinuatingLoop, self).__init__()
        self._delay = delay

    def _wait(self):
        time.sleep(self._delay)

if __name__ == "__main__":
    game = ContinuatingLoop(.25)
    game.main_loop()
