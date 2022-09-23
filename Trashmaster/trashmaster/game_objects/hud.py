import pygame
import settings as s

class HUD(pygame.sprite.Sprite):
    def  __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load('./resources/textures/misc/hud.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = s.HEIGHT - self.rect.height
        # self.rect.x = s.WIDTH - self.rect.height
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y