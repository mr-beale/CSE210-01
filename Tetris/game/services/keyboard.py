from pyray import *
class KeyboardService:

    def __init__(self):
        self._keys = {}
        
        self._keys['left'] = KEY_LEFT
        self._keys['right'] = KEY_RIGHT
        self._keys['down'] = KEY_DOWN
        self._keys['space'] = KEY_SPACE
        self._keys['enter'] = KEY_ENTER

    def is_key_up(self, key):
        pyray_key = self._keys[key.lower()]
        return is_key_up(pyray_key)

    def is_key_pressed(self, key):
        pyray_key = self._keys[key.lower()]
        return is_key_pressed(pyray_key)

    def is_key_down(self, key):
        pyray_key = self._keys[key.lower()]
        return is_key_down(pyray_key)