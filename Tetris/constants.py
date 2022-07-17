from game.shared.color import Color


COLUMNS = 10
ROWS = 18
CELL_SIZE = 20
MAX_X = CELL_SIZE * COLUMNS + 160
MAX_Y = CELL_SIZE * ROWS
GRID_X = CELL_SIZE * COLUMNS
GRID_Y = CELL_SIZE * ROWS
FRAME_RATE = 30
FONT_SIZE = 19
CAPTION = "Tetris"

RED = Color(240, 0, 0)
YELLOW = Color(240, 240, 0)
GREEN = Color(0, 240, 0)
CYAN = Color(0, 240, 240)
ORANGE = Color(240, 160, 0)
VIOLET = Color(160, 0, 240)
BLUE = Color(0, 0, 240)

BLACK = Color(0, 0, 0)
GRAY = Color(120, 120, 120).to_tuple()
