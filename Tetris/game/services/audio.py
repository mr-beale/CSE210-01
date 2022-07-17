from pyray import *

class AudioService:

    def loadMusic(self):
        init_audio_device()
        
        self.music = load_music_stream("C:\\Users\\myste\\Documents\\CSE210\\CSE210-01\\Tetris\\game\\assets\\Korobeiniki.wav")
        #self.music = Music(self._track['main'], 2416448, True, None, None)

    def play(self):
        play_music_stream(self.music)

    def refreshMusic(self):
        update_music_stream(self.music)

    def setSpeed(self, speed):
        set_music_pitch(self.music, speed)