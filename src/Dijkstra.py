from Readrer import read_data
import os
from Vertex import Vertex
from matplotlib import pyplot as plt
import time


def dijkstra(graph_name, end, start=0, draw=False, entire=False):
    vertices: Vertex
    vertices = read_data(graph_name, draw=draw, entire=entire)
    distances = [None] * len(vertices)
    open_vertices = []
    closed_vertices = []
    open_vertices.append(vertices[start])
    distances[start] = 0
    vertices[start].set_reached()
    while len(open_vertices) != 0:
        v = open_vertices.pop()             # Current vertex
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
                    vertices[vertex].set_back_pointer(v.get_ver_num())
                elif predict_distance < distances[vertex]:
                    distances[vertex] = predict_distance
                    vertices[vertex].set_back_pointer(v.get_ver_num())
                    open_vertices.append(vertices[vertex])
                else:
                    pass
                edge_num += 1
            pass

    # print(distances)
    if distances[end] is not None:
        print('Result = ', distances[end])
    else:
        print('Cannot reach the vertex')


    if draw:
        tracker = vertices[end].get_back_pointer()
        current_pos = vertices[end].get_pos()
        print(end)
        while tracker is not None:
            print(tracker)
            x, y = vertices[tracker].get_pos()
            x = [current_pos[0], x]
            y = [current_pos[1], y]
            plt.plot(x, y, 'r.-', linewidth=1)
            current_pos = vertices[tracker].get_pos()
            tracker = vertices[tracker].get_back_pointer()

        end_x, end_y = vertices[end].get_pos()
        plt.quiver(end_x, end_y - 10, 0, 1, color='r', width=0.005)

        plt.ioff()
        plt.show()

        # print(vertices[0].get_square_pos())

    return distances[end]

time_start = time.time()
dijkstra('graph1000_0.1', 83, start=0, draw=True, entire=False)
time_end = time.time()
print('Time cost = %fs' % (time_end - time_start))
