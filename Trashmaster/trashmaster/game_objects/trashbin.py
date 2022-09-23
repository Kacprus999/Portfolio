import pygame as pg
from enum import Enum
from random import randrange
from map.tile import Tile
class Trashbin(Tile):
    def __init__(self, img, x, y, width, height):
        super().__init__(img, x, y, width, height)

        self.x = x
        self.y = y
        
        self.season = randrange(4)
        self.trash_type = randrange(5)
        self.mass = randrange(5)
        self.space = randrange(5)
        self.trash_mass = randrange(5)


    def get_coords(self):
        return (self.x, self.y)

    def get_attributes(self):
        return (self.season, self.trash_type, self.mass, self.space, self.trash_mass) 
