import wx
from wx.lib import newevent
from board import Board
from engine import Engine


evt_speed_changed, EVT_SPEED = newevent.NewEvent()


class WxRenderer(wx.App):
    def __init__(self):
        self._timer = None
        self._board = None
        self._engine = None
        self._gui = None
        self._speed = 500
        super(WxRenderer, self).__init__(False)

    def OnInit(self):
        self._board = Board(30, 30)
        self._engine = Engine(self._board)
        self._gui = MainFrame(self._board)
        self._gui.Show()

        self._timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._iterate, self._timer)
        self.Bind(EVT_SPEED, self._update_speed)

        self._init_game_board()

        self._timer.Start(self._speed)

        return True

    def _iterate(self, evt):
        self._engine.step()
        self._gui.Refresh()
        self._timer.Start(self._speed)

    def _init_game_board(self):
        #glider
        self._board.get(6, 6).alive = True
        self._board.get(7, 7).alive = True
        self._board.get(7, 8).alive = True
        self._board.get(6, 8).alive = True
        self._board.get(5, 8).alive = True

        #blinker
        self._board.get(12, 4).alive = True
        self._board.get(12, 5).alive = True
        self._board.get(12, 6).alive = True

    def _update_speed(self, evt):
        self._speed = evt.new_speed


class MainFrame(wx.Frame):
    def __init__(self, board):
        super(MainFrame, self).__init__(None)

        panel = GridCtrl(self, board, show_lines=False)
        self.speed_slider = wx.Slider(self, minValue=100, maxValue=1500)
        self.speed_value = wx.StaticText(self, label="NA")

        sizer_speed = wx.BoxSizer(wx.HORIZONTAL)
        sizer_speed.Add(self.speed_slider, 1, wx.EXPAND)
        sizer_speed.Add(self.speed_value, 0, wx.EXPAND)
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        sizer_main.Add(sizer_speed, 0, wx.EXPAND)
        sizer_main.Add(panel, 1, wx.EXPAND)

        self.SetSizer(sizer_main)

        self.Bind(wx.EVT_SLIDER, self._on_slider_changed, self.speed_slider)

        self.SetSize((500, 500))

        self.speed_slider.SetValue(100)
        self._on_slider_changed(None)

    def _on_slider_changed(self, evt):
        new_value = self.speed_slider.GetValue()
        self.speed_value.SetLabel(str(new_value))
        wx.PostEvent(self, evt_speed_changed(new_speed=new_value))


class Cell(object):
    def __init__(self, x, y, color=None):
        if color is None:
            color = wx.Colour(0, 0, 0)

        self.color = color
        self.x = x
        self.y = y


class GridCtrl(wx.Panel):
    def __init__(self, parent, board, show_lines=True):
        super(GridCtrl, self).__init__(parent)

        self._board = board
        self._width = board.width
        self._height = board.height
        self._show_lines = show_lines
        self._canvas_w = 0
        self._canvas_h = 0
        self._cell_width = 0
        self._cell_height = 0

        self._cell_brush = wx.Brush("grey", wx.SOLID)

        self._cells = []

        self._cells.append(Cell(3, 2))

        self.Bind(wx.EVT_PAINT, self._on_paint)

    def _on_paint(self, evt):
        dc = wx.PaintDC(self)
        dc.Clear()
        self._canvas_w, self._canvas_h = self.GetSize()
        self._cell_width = self._canvas_w / self._width
        self._cell_height = self._canvas_h / self._height

        if self._show_lines:
            self._draw_grid_lines(dc)

        self._draw_cells(dc)

    def _draw_grid_lines(self, dc):
        dc.DrawLine(0, 0, self._canvas_w, 0)
        dc.DrawLine(0, 0, 0, self._canvas_h)
        dc.DrawLine(self._canvas_w, 0, self._canvas_w, self._canvas_h)
        dc.DrawLine(0, self._canvas_h, self._canvas_w, self._canvas_h)

        for y in range(0, self._height):
            dc.DrawLine(0, y * self._cell_height, self._canvas_w, y * self._cell_height)

        for x in range(0, self._width):
            dc.DrawLine(x * self._cell_width, 0, x * self._cell_width, self._canvas_w)

    def _draw_cells(self, dc):
        dc.SetBrush(self._cell_brush)
        for cell in self._board:
            if cell.is_alive:
                self._draw_cell(cell, dc)

    def _draw_cell(self, cell, dc):
        dc.DrawRectangle(cell.pos.x * self._cell_width,
                         cell.pos.y * self._cell_height,
                         self._cell_width + 1,
                         self._cell_height + 1)


if __name__ == "__main__":
    app = WxRenderer()
    app.MainLoop()
