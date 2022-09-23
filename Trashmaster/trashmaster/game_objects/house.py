import pygame.image
from typing import Optional
import os
from random import randint

class House(pygame.sprite.Sprite):
    
    def __init__(self, x:int, y:int,
    number_of_bins:int = 0, if_exist: bool = False):

        super().__init__()   
        self.number_of_bins = number_of_bins
        self.x = x
        self.y = y
        self.if_exist = if_exist
        self.bin_id: Optional[int]
        self.base_path = "./resources/textures/buliding/"
        # Statyczny sprite domku, obecnie randomny
        # self.image = pygame.image.load("./resources/textures/buliding/GTA2_TILE_112.bmp")
        self.image = pygame.image.load(f"{self.base_path}{self.get_random_house_texture()}")
        

    def get_random_house_texture(self):
        files = os.listdir(self.base_path)
        value = randint(0, len(files)-1)
        return files[value]