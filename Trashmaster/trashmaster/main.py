import os
import sys
from random import randint
import math

import pygame as pg
import numpy

from game_objects.player import Player
from game_objects.aiPlayer import aiPlayer
from game_objects.trash import Trash

from map import map
from map import map_utils
from settings import *
from path_search_algorthms import bfs
from path_search_algorthms import a_star_controller, a_star
from decision_tree import decisionTree
from NeuralNetwork import prediction
from game_objects.trash import Trash
from genetic_algorithm import TSP
from game_objects import aiPlayer
import itertools


def getTree():
    tree = decisionTree.tree()
    decisionTree.tree_as_txt(tree)
    # decisionTree.tree_to_png(tree)
    decisionTree.tree_to_structure(tree)
    drzewo = decisionTree.tree_from_structure('./decision_tree/tree_model')
    # print("Dla losowych danych predykcja czy wziąć kosz to: ")
    # dec = decisionTree.decision(drzewo, *(4,1,1,1))
    # print('---')
    # print(f"decision is{dec}")
    # print('---')

    return drzewo


class Game():

    def __init__(self):
        pg.init()
        pg.font.init()
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS) / 333.0
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Trashmaster")
        self.load_data()
        self.init_game()
        self.t = aiPlayer.aiPlayer(self.player, game=self)

    def init_game(self):
        # initialize all variables and do all the setup for a new game

        self.text_display = ''

        # sprite groups and map array for calculations
        (self.roadTiles, self.wallTiles, self.trashbinTiles), self.mapArray = map.get_tiles()

        # save current map
        file = open('last_map.nparr', 'wb')
        numpy.save(file, self.mapArray, allow_pickle=True)
        file.close

        self.trashDisplay = pg.sprite.Group()
        self.agentSprites = pg.sprite.Group()
        # player obj
        self.player = Player(self, 32, 32)
        # camera obj
        self.camera = map_utils.Camera(MAP_WIDTH_PX, MAP_HEIGHT_PX)

        # other
        self.debug_mode = False

    def init_bfs(self):
        start_node = (0, 0)
        target_node = (18, 18)
        find_path = bfs.BreadthSearchAlgorithm(start_node, target_node, self.mapArray)
        path = find_path.bfs()
        # print(path)
        realPath = []
        nextNode = target_node
        for i in range(len(path) - 1, 0, -1):
            node = path[i]
            if node[0] == nextNode:
                realPath.insert(0, node[0])
                nextNode = node[1]
        print(realPath)

    def init_decision_tree(self):
        # logika pracy z drzewem
        self.positive_decision = []
        self.negative_decision = []

        for i in self.trashbinTiles:
            atrrs_container = i.get_attributes()
            x, y = i.get_coords()
            dec = decisionTree.decision(getTree(), *atrrs_container)
            if dec[0] == 1:
                self.positive_decision.append(i)     # zmiana po to by losowało wszystkie smietniki a nie poprawne tylko, zeby ladniej bylo widac algorytm genetyczny
            else:
                self.negative_decision.append(i)

        print('positive actions')
        print(len(self.positive_decision))
        # print('positive actions')
        # for i in self.positive_actions:
        #     print('----')
        #     print(i)
        #     print('----')
        self.draw()
    def decsion_tree_move(self):
        
        for i in range(0,len(self.positive_decision)):
            # print(i.get_coords())
            print('action')
            
            
            
            temp_tsp = str(self.tsp_list[i])
            temp_tsp = temp_tsp.strip("()")
            temp_tsp = temp_tsp.split(",")
            trash_x = int(temp_tsp[0])
            trash_y = int(temp_tsp[1])

          
            print(trash_x, trash_y)

            action = a_star_controller.get_actions_for_target_coords(trash_x, trash_y, self)

            print(action)
            self.t.startAiController(action)

            print('')
            print('--rozpoczecie sortowania smietnika--')
            dir = "./resources/trash_dataset/test/all"
            files = os.listdir(dir)
            for j in range(0, 10):
                random = randint(0, 48)
                file = files[random]
                result = prediction.getPrediction(dir + '/' + file, 'trained_nn_20.pth')
                img = pg.image.load(dir + '/' + file).convert_alpha()
                img = pg.transform.scale(img, (128, 128))
                offset_x, offset_y = self.camera.offset()
                trash = Trash(img, math.floor(-offset_x * TILESIZE), math.floor(-offset_y * TILESIZE), 128, 128)
                self.trashDisplay.empty()
                self.trashDisplay.add(trash)
                self.text_display = result
                self.draw()
                pg.time.wait(100)
            self.text_display = ''
            self.trashDisplay.empty()
            self.draw()

        # print(self.positive_actions[0])

    def init_TSP(self):
        
        city_list =[]

        for i in self.positive_decision:
            trash_x, trash_y = i.get_coords()
            city_list.append(TSP.City(x=trash_x, y=trash_y, array=self.mapArray))
        
        self.tsp_list = TSP.geneticAlgorithmPlot(population=city_list, popSize=100, eliteSize=20, mutationRate=0.01, generations=500, array=self.mapArray)
        print(self.tsp_list)

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'resources/textures')

        self.player_img = pg.image.load(os.path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        self.init_decision_tree()
        self.init_TSP()
        self.decsion_tree_move()

        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.agentSprites.update()
        self.camera.update(self.player)
        # pygame.display.update()

    def draw(self):
        # display fps as window title
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))

        # rerender map
        map.render_tiles(self.roadTiles, self.screen, self.camera)
        map.render_tiles(self.wallTiles, self.screen, self.camera, self.debug_mode)
        map.render_tiles(self.trashbinTiles, self.screen, self.camera)
        map.render_tiles(self.trashDisplay, self.screen, self.camera)

        # draw text
        text_surface = pg.font.SysFont('Comic Sans MS', 30).render(self.text_display, False, (255, 255, 255))
        self.screen.blit(text_surface, (0, 128))

        # rerender additional sprites
        for sprite in self.agentSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.debug_mode:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)

        # self.player.hud_group.draw(self.screen)
        # finally update screen
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.debug_mode = not self.debug_mode
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                offset_x, offset_y = self.camera.offset()
                clicked_coords = [math.floor(pos[0] / TILESIZE) - offset_x, math.floor(pos[1] / TILESIZE) - offset_y]
                actions = a_star_controller.get_actions_by_coords(clicked_coords[0], clicked_coords[1], self)

                if (actions != None):
                    self.t.startAiController(actions)


# create the game object

if __name__ == "__main__":
    g = Game()

    g.run()
    g.show_go_screen()