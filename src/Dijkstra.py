from Readrer import read_file
import os
from Vertex import Vertex


edges_data = []
vertices_data = []

def read_data():
    edges_data = read_file('D:\\PyProject\\UninformedAndInformedSearch\\Uninformed_And_Informed_Search\\data\\graph100_0.1\\e.txt')
    vertices_data = read_file('D:\\PyProject\\UninformedAndInformedSearch\\Uninformed_And_Informed_Search\\data\\graph100_0.1\\v.txt')
    print(len(vertices_data))

    vertices = [0] * len(vertices_data)
    for edge in edges_data:
        start, end, distance = edge.split(',')
        start = int(start)
        end = int(end)
        distance = float(distance)
        if vertices[start] == 0:
            vertices[start] = Vertex(start)
            vertices[start].add_edge(end, distance)
        else:
            vertices[start].add_edge(end, distance)

    print(vertices[1].get_connected_edge())
    print(vertices[1].get_connected_distance())
    print(vertices[1].get_ver_num())

    return vertices


def dijkstra(start, end):
    vertices = read_data()
    distances = [None] * len(vertices_data)
    for e in range(0, len(vertices)):
        pass

dijkstra(0, 0)