import pygame as pg 

class Keys:
  def __init__(self):
    self.keys = {
      ord("w"):False,
      ord("d"):False,
      ord("s"):False,
      ord("a"):False,
      pg.K_SPACE:False
    }
  
  def update(self):
    for ev in pg.event.get():
      if ev.type == pg.KEYDOWN:
        if ev.key in self.keys:
          self.keys[ev.key] = True
      
      elif ev.type == pg.KEYUP:
        if ev.key in self.keys:
          self.keys[ev.key] = False

      elif ev.type == pg.K_RIGHT:
        if ev.key in self.keys:
          self.keys[ev.key] = True

      elif ev.type == pg.K_LEFT:
        if ev.key in self.keys:
          self.keys[ev.key] = True

      elif ev.type == pg.K_SPACE:
        if ev.key in self.keys:
          self.keys[ev.key] = True

