import math
from path_search_algorthms import a_star
from settings import *

def get_actions_by_coords(x, y, game):
        # print('get_actions_by_coords')
        # print(x, y, x/TILESIZE, y/TILESIZE)
        offset_x, offset_y = game.camera.offset()
        # print('offset ' + str(self.camera.offset()))
        clicked_coords = [math.floor(x / TILESIZE) - offset_x, math.floor(y / TILESIZE) - offset_y]
        # print(self.player.pos[0], self.player.pos[1], clicked_coords)
        actions = a_star.search_path(math.floor(game.player.pos[0] / TILESIZE),
                                        math.floor(game.player.pos[1] / TILESIZE), game.player.rotation(),
                                        clicked_coords[0], clicked_coords[1], game.mapArray)
        return actions

def get_actions_for_target_coords(x, y, game):
    actions = a_star.search_path(
        math.floor(game.player.pos[0] / TILESIZE),
        math.floor(game.player.pos[1] / TILESIZE),
        game.player.rotation(),
        x / TILESIZE,
        y / TILESIZE,
        game.mapArray
    )
    return actions