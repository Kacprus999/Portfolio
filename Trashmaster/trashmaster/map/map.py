from map import map_utils
from map import map_pattern
import pygame as pg
from settings import *

def get_tiles():
    array = map_utils.generate_map()
    pattern = map_pattern.get_pattern()
    tiles = map_utils.get_sprites(array, pattern)
    return tiles, array

def render_tiles(tiles, screen, camera, debug=False):
    for tile in tiles:
        screen.blit(tile.image, camera.apply_rect(tile.rect))
        if debug:
            pg.draw.rect(screen, RED, camera.apply_rect(tile.rect), 1)
