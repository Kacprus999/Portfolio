from path_search_algorthms import a_star_utils
import pygame as pg
from settings import *
from game_objects import utils
from game_objects.hud import HUD

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.agentSprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.__rotation = a_star_utils.Rotation.RIGHT
        self.mass = 0

        self.hud = HUD()
        self.hud_group = pg.sprite.Group()
        self.hud_group.add(self.hud)

    def rotation(self) -> a_star_utils.Rotation:
        return self.__rotation

    def set_rotation(self, rotation):
        self.__rotation = rotation
        if (rotation == a_star_utils.Rotation.UP or rotation == int(a_star_utils.Rotation.UP)):
            self.rot = -90
        elif (rotation == a_star_utils.Rotation.RIGHT or rotation == int(a_star_utils.Rotation.RIGHT)):
            self.rot = 0
        elif (rotation == a_star_utils.Rotation.DOWN or rotation == int(a_star_utils.Rotation.DOWN)):
            self.rot = 90
        elif (rotation == a_star_utils.Rotation.LEFT or rotation == int(a_star_utils.Rotation.LEFT)):
            self.rot = 180

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)


    def update(self):
        self.get_keys()
        # must be fix for manual movement
        # self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        image_rotation = self.rot
        if(abs(image_rotation) == 90):
            image_rotation *= -1
        self.image = pg.transform.rotate(self.game.player_img, image_rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        utils.collide_with_walls(self, self.game.wallTiles, 'x')
        self.hit_rect.centery = self.pos.y
        utils.collide_with_walls(self, self.game.wallTiles, 'y')
        self.rect.center = self.hit_rect.center

        self.hud_group.update()
        
    def get_actual_coords(self):
        # return (self.rect.x / 64, self.rect.y / 64)
        return (self.rect.x, self.rect.y)