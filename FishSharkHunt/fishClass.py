import pygame as pg 

class Fishy:
    def __init__ (self, surface, rect):
        self.surface = pg.transform.scale(surface, (rect.width, rect.height))
        self.rect = rect


  

