from game.shared.point import Point
from pyray import *
from constants import *

class VideoService:

    def open_window(self):

        init_window(MAX_X, MAX_Y, CAPTION)
        set_target_fps(FRAME_RATE)

    def running(self):
        return(not window_should_close())

    def start_drawing(self):
        begin_drawing()
        clear_background(WHITE)
        self._draw_grid()

    def stop_drawing(self):
        end_drawing()

    def exit(self):
        close_window()

    def draw_block(self, item):
        squares = item.get_squares()
        color = item.get_color().to_tuple()
        size = FONT_SIZE

        for square in squares:
            x = square.get_position().get_x()
            y = square.get_position().get_y()
            draw_rectangle(x, y, size, size, color)

    def draw_blocks(self, items):
        for item in items:
            self.draw_block(item)

    def draw_label(self, item):
        text = item.get_text()
        color = item.get_color().to_tuple()
        size = FONT_SIZE
        x = item.get_position().get_x()
        y = item.get_position().get_y()

        draw_text(text, x, y, size, color)

    def draw_labels(self, items):
        for item in items:
            self.draw_label(item)

    def _draw_grid(self):
        for y in range(0, GRID_Y+1, CELL_SIZE):
            draw_line(0, y, GRID_X, y, GRAY)
        for x in range(0, GRID_X+1, CELL_SIZE):
            draw_line(x, 0, x, GRID_Y, GRAY)