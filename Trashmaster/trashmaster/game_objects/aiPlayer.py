from game_objects.player import Player
import pygame as pg
import math
from settings import *
vec = pg.math.Vector2

class aiPlayer():
    def __init__(self, player, game):
        self.player : Player = player
        self.game = game

    def moveAiPlayer(self):
        for i in range(64 * 1):
            self.player.pos += vec(1, 0).rotate(self.player.rot)
            self.player.rect.center = self.player.pos
            # print(f'START COORDS: {x_s, x_bias}; CURRENT AGENT COORDS: {self.player.get_actual_coords()}')
            self.game.update()
            self.player.update()
            self.game.draw()
            # print(self.player.get_actual_coords())
        

    def turn_left(self):
        change = int(self.player.rotation()) - 1
        if(change == -1):
            change = 3
        self.player.set_rotation(change)

    def turn_right(self):
        change = int(self.player.rotation()) + 1
        if(change == 4):
            change = 0
        self.player.set_rotation(change)

    def startAiController(self, actions):
        for action in actions:
            if action == 'forward':
                self.moveAiPlayer()
                # print(f'ROT IS {self.player.rot}')
            if action == 'right':
                self.turn_right()
            if action == 'left':
                self.turn_left()
        # print(f'ROT: {self.player.rot}')
        # print("Agent pos: ", math.floor(self.player.pos[0] / TILESIZE), math.floor(self.player.pos[1] / TILESIZE))