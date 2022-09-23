from map import map_utils
from path_search_algorthms import a_star, a_star_utils
import numpy

file = open('last_map.nparr', 'rb')
array = numpy.load(file)
file.close

actions = a_star.search_path(12, 0, a_star_utils.Rotation.UP, 1, 5, array)
print(actions)