class Library:
    def __init__ (self, brick):
      self.brick = brick
    def beep(self):
      self.brick.sound.beep(440, 500)