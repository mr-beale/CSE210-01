from pyray import *
from constants import *
from game.services.video import VideoService
from game.services.audio import AudioService
from game.graphics import Graphics

vs = VideoService()
audio = AudioService()
gp = Graphics()

vs.open_window()
audio.loadMusic()
audio.play()
gp.newBlock()

while vs.running():
    if not gp.game_over:
        blocks = gp.getBlocks()
        audio.setSpeed(gp.speed)
        audio.refreshMusic()
        vs.start_drawing()
        vs.draw_labels(gp.labels)
        vs.draw_block(gp.next_block)
        vs.draw_blocks(blocks)
        gp.moveBlock()
    else:
        draw_text("GAME OVER", CELL_SIZE, (MAX_Y//2)-22, 27, BLACK.to_tuple())
    vs.stop_drawing()    
vs.exit()

