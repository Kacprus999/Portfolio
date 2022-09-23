from enum import Enum

from map import map_utils
from settings import *


class Rotation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    NONE = 100

    def __int__(self):
        return self.value


class Node:
    def __init__(self, x: int, y: int, rotation: Rotation):
        self.x = x
        self.y = y
        self.g_cost = 0
        self.h_cost = 0
        self.parent: Node | bool = False
        self.rotation: Rotation = rotation

    def f_cost(self):
        return self.g_cost + self.h_cost


def get_neighbours(node, searched_list, array):
    neighbours = []
    for offset_x in range(-1, 2):
        for offset_y in range(-1, 2):
            # don't look for cross neighbours
            if (abs(offset_x) + abs(offset_y) == 1):
                x = node.x + offset_x
                y = node.y + offset_y
                # prevent out of map coords
                if (x >= 0 and x < MAP_WIDTH and y >= 0 and y < MAP_HEIGHT):
                    if (map_utils.isRoadTile(array[y][x]) and (x, y) not in searched_list):
                        neighbour = Node(x, y, Rotation.NONE)
                        neighbour.rotation = get_needed_rotation(node, neighbour)
                        neighbours.append(neighbour)
    return neighbours


# move cost schema:
# - move from tile to tile: 10
# - add extra 10 (1 rotation) if it exists
def get_h_cost(start_node: Node, target_node: Node):
    distance_x = abs(start_node.x - target_node.x)
    distance_y = abs(start_node.y - target_node.y)
    cost = (distance_x + distance_y) * 10

    if (distance_x > 0 and distance_y > 0):
        cost += 10

    return cost


# move cost schema:
# - move from tile to tile: 10
# - every rotation 90*: 10
def get_neighbour_cost(start_node: Node, target_node: Node) -> int:
    new_rotation = get_needed_rotation(start_node, target_node)
    rotate_change = abs(get_rotate_change(start_node.rotation, new_rotation))
    if (rotate_change == 0):
        return 10
    elif (rotate_change == 1 or rotate_change == 3):
        return 20
    else:
        return 30


# translate rotation change to move
def get_move(start_node: Node, target_node: Node):
    rotate_change = get_rotate_change(start_node.rotation, target_node.rotation)
    if (rotate_change == 0):
        return ["forward"]
    if (abs(rotate_change) == 2):
        return ["right", "right", "forward"]
    if (rotate_change == -1 or rotate_change == 3):
        return ["right", "forward"]
    else:
        return ["left", "forward"]


# simple calc func
def get_rotate_change(rotationA: Rotation, rotationB: Rotation) -> int:
    return int(rotationA) - int(rotationB)


# get new rotation for target_node as neighbour of start_node
def get_needed_rotation(start_node: Node or bool, target_node: Node) -> Rotation:
    if(start_node == False):
        return target_node.rotation
    if (start_node.x - target_node.x > 0):
        return Rotation.LEFT
    if (start_node.x - target_node.x < 0):
        return Rotation.RIGHT
    if (start_node.y - target_node.y > 0):
        return Rotation.UP
    if (start_node.y - target_node.y < 0):
        return Rotation.DOWN





