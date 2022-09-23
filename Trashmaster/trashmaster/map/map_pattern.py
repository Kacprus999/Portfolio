import os
import pygame as pg

HERE_DIR = os.path.abspath(os.path.dirname(__file__))
TEXTURES_DIR = HERE_DIR.rpartition(os.sep)[0]+"\\resources\\textures"

ROAD_DIR = TEXTURES_DIR+"\\road\\"
BUILDING_DIR = TEXTURES_DIR+"\\buliding\\"

def load_img(path):
    return pg.image.load(path).convert_alpha()

def get_pattern():
    return {
        0: load_img("resources/textures/road/GTA2_TILE_257.bmp"),
        1: load_img("resources/textures/buliding/GTA2_TILE_187.bmp")
    }

def get_trashbin_pattern():
    return {
        0: load_img("resources/textures/misc/trash_bin_small_bio.png"),
        1: load_img("resources/textures/misc/trash_bin_small_glass.png"),
        2: load_img("resources/textures/misc/trash_bin_small_plastic.png"),
        3: load_img("resources/textures/misc/trash_bin_small_paper.png"),
        4: load_img("resources/textures/misc/trash_bin_small.png")
    }