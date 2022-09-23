from re import X
import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pg.Surface([width, height], pg.SRCALPHA, 32)
        self.image.blit(img, (0,0))

        self.rect = pg.Rect(x, y, width, height)
