import pygame as pg
from enum import Enum
from random import randrange
from map.tile import Tile
class Trash(Tile):
    def __init__(self, img, x, y, width, height):
        super().__init__(img, x, y, width, height)

        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

