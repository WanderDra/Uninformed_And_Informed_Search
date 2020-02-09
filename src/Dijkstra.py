from Readrer import read_data
import os
from Vertex import Vertex


def dijkstra(start, end):
    vertices = read_data(draw=False)
    distances = [None] * len(vertices)
    open_vertices = []
    closed_vertices = []
    open_vertices.append(vertices[start])
    distances[start] = 0
    while len(open_vertices) != 0:
        v = open_vertices.pop()
        current_distance = 0
        if distances[v.get_ver_num()] is None:
            current_distance = 0
        else:
            current_distance = distances[v.get_ver_num()]
        connected_edge = v.get_connected_edge()
        connected_distance = v.get_connected_distance()
        edge_num = 0
        if connected_edge:
            for vertex in connected_edge:
                if vertices[vertex].is_reached() is not True:
                    open_vertices.append(vertices[vertex])
                    vertices[vertex].set_reached()
                predict_distance = connected_distance[edge_num] + current_distance
                if distances[vertex] is None:
                    distances[vertex] = predict_distance
                elif predict_distance < distances[vertex]:
                    distances[vertex] = predict_distance
                else:
                    pass
                edge_num += 1
            pass

    print(distances)
    if distances[end] is not None:
        print('Result = ', distances[end])
    else:
        print('Cannot reach the vertex')


dijkstra(41, 41)