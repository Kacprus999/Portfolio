import pygame as pg

class Dump(pg.sprite.Sprite):
    # wysypisko
    def __init__(self):
        super().__init__()   
        self.glass = []
        self.paper = []
        self.bio = []
        self.other_trash = []