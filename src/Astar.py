from Vertex import Vertex
from Readrer import read_data
import math


def astar(start, end, draw=False):
    vertices: Vertex
    vertices = read_data(draw=draw)
    s_x, s_y = vertices[start].get_square_pos()
    e_x, e_y = vertices[end].get_square_pos()
    # h(x)
    h = int(math.sqrt(((e_x - s_x) * 10) ** 2 + ((e_y - s_y) * 10) ** 2))
    print(h)
    




astar(0, 51)