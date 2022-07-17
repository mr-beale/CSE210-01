from game.hud import HUD_element
from game.shared.point import Point
from game.blocks.I_Block import I_block
from game.blocks.J_Block import J_block
from game.blocks.L_Block import L_block
from game.blocks.O_Block import O_block
from game.blocks.S_Block import S_block
from game.blocks.T_Block import T_block
from game.blocks.Z_Block import Z_block
from constants import *
from random import choice
from game.services.keyboard import KeyboardService

class Graphics:
    def __init__(self):
        self.score = 0
        self.lines = 0
        self.level = 0
        self.speed = 1.0
        self.down = 1
        self.game_over = False
        self.setLabels()
        self.blocks = []
        self.labels = [self.scoreLabel, self.scoreText, self.levelLabel, self.currentLevel, self.linesLabel, self.linesCleared, self.nextLabel]
        self.nextBlock()
        self._keys = KeyboardService()
        
            
    def getBlocks(self):
        return(self.blocks)

    def setLabels(self):
        self.scoreLabel = HUD_element(Point(CELL_SIZE*(COLUMNS+1), 2), BLACK, "SCORE")
        self.scoreText = HUD_element(Point(CELL_SIZE*(COLUMNS+1), self.scoreLabel.get_position().get_y()+CELL_SIZE), BLACK, "0")
        self.levelLabel = HUD_element(Point(CELL_SIZE*(COLUMNS+1), CELL_SIZE*3), BLACK, "LEVEL:")
        self.currentLevel =  HUD_element(Point(CELL_SIZE*(COLUMNS+1), self.levelLabel.get_position().get_y()+CELL_SIZE), BLACK, "0")
        self.linesLabel = HUD_element(Point(CELL_SIZE*(COLUMNS+1), CELL_SIZE*6), BLACK, "LINES:")
        self.linesCleared = HUD_element(Point(CELL_SIZE*(COLUMNS+1), self.linesLabel.get_position().get_y()+CELL_SIZE), BLACK, "0")
        self.nextLabel = HUD_element(Point(CELL_SIZE*(COLUMNS+1), CELL_SIZE*9), BLACK, "NEXT BLOCK:")

    def nextBlock(self):
        blockTypes = [I_block, T_block, J_block, L_block, Z_block, S_block, O_block]
        self.next_block = choice(blockTypes)()
        
    def newBlock(self):
            self.next_block.set_position(Point(CELL_SIZE*5, -CELL_SIZE))
            self.next_block.zero_deg()
            self.blocks.append(self.next_block)
            self.nextBlock()

    def moveBlock(self):
        minY, maxY, minX, maxX = self.blocks[-1].get_limits()
        side = 0
        down = self.down

        if self._keys.is_key_pressed('left'):
            if minX - CELL_SIZE >= 0:
                side = -CELL_SIZE
        if self._keys.is_key_pressed('right'):
            if maxX + CELL_SIZE <= COLUMNS*CELL_SIZE:
                side = CELL_SIZE
        if self._keys.is_key_down('down'):
            if self.blocks[-1].get_position().get_y() % CELL_SIZE == 0:
                down = CELL_SIZE

        if self._keys.is_key_pressed('space'):
            self.blocks[-1].rotate_block()

        
        if maxY < MAX_Y and not self.stack_blocks(self.blocks[-1].get_squares()):
            self.blocks[-1].set_position(self.blocks[-1].get_position().add(Point(side, down)))
        else:
            self.clear_row()
            self.newBlock()

        self.blocks[-1].get_rotation()

    def moveBlocks(self):
        for block in self.blocks:
            stacked = self.stack_blocks(block.get_squares())
            for square in block.get_squares():
                if square.get_position().get_y() < MAX_Y-CELL_SIZE and not stacked:
                    square.set_position(square.get_position().add(Point(0, CELL_SIZE)))

    def stack_blocks(self, squares):
        placed = self.blocks.copy()
        placed.pop(-1)
        for box in placed:
            for square in squares:
                for block in box.get_squares():
                    if square.get_position().get_x() == block.get_position().get_x() and square.get_position().get_y() + CELL_SIZE == block.get_position().get_y():
                        if square.get_position().get_y() < 0: self.game_over = True
                        return(True)

        return(False)

    
    def clear_row(self):
        to_remove = []
        cleared = 0

        rows = self.get_rows()

        for row in rows.keys():
            if self.row_is_full(rows[row]): to_remove.append(rows[row])

        for row in to_remove:
            self.delete_row(row)
                    
        self.cascade()

        #self.moveBlocks()
        cleared = len(to_remove)
        self.update_score(cleared, self.level)
        self.update_lines(cleared)
        self.update_level(self.lines)
                        
    def get_rows(self):
        rows = {}
        for i in range(0, ROWS):
            in_this_row = []
            for block in self.blocks:
                for square in block.get_squares():
                    if square.get_position().get_y() == i*CELL_SIZE: in_this_row.append((block, square))

            rows[f'row{i+1}'] = in_this_row
        return(rows)


    def row_is_full(self, row):
        if len(row) >= 10:
            return(True)
        return(False)

    def delete_row(self, row):
        for square in row:
            square[0].remove_square(square[1])

    def cascade(self):
        rows = self.get_rows()
        for i, row in enumerate(rows.keys()):
            if len(rows[row]) == 0:
                for j in range(0, i):
                    for square in list(rows.values())[j]:
                        square[1].set_position(square[1].get_position().add(Point(0, CELL_SIZE)))

    def clear_all(self):
        for block in self.blocks:
            for square in block.get_squares():
                block.remove_square(square)
                
    def update_score(self, cleared, level):
        points = {"1": (level+1)*40,
                  "2": (level+1)*100,
                  "3": (level+1)*300,
                  "4": (level+1)*1200}

        if cleared <= 0:
            return
        else:
            self.score += int(points[f'{cleared}'])
            self.scoreText.set_text(f"{self.score}")

    def update_lines(self, cleared):
        if cleared > 0:
            self.lines += cleared
            self.linesCleared.set_text(f"{self.lines}")

    def update_level(self, lines):
        self.level = (lines//10)
        self.speed = 1+self.level*0.005

        if self.level > 0 and self.level % 2 == 0:
            rates = [2, 4, 5, 10, 20]
            self.down = rates[int(self.level/2)]
        else: self.down = 1

        self.currentLevel.set_text(f"{self.level}")