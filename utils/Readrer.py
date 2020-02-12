from Vertex import Vertex
from matplotlib import pyplot as plt
import numpy as np
import os


def read_file(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            if line[0] != '#':
                data.append(line)
    return data


def read_data(graph_name, draw=False, entire=False):

    paths = os.path.abspath(os.path.dirname(__file__)).split('shippingSchedule')[0].split('\\')[:-1]
    project_dir = paths[0]
    paths.pop(0)
    for path in paths:
        project_dir += os.sep + path

    edges_data = read_file(
        os.path.join(project_dir, 'data', graph_name, 'e.txt'))
    vertices_data = read_file(
        os.path.join(project_dir, 'data', graph_name, 'v.txt'))
    print(len(vertices_data))

    vertices = [0] * len(vertices_data)

    for vertex in vertices_data:
        index, square = vertex.split(',')
        index = int(index)
        square = int(square)
        if vertices[index] == 0:
            vertices[index] = Vertex(index)
            vertices[index].set_square(square)

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

    if draw is True:
        plt.figure()
        plt.ion()
        blocks = []
        col = []
        row = []
        # Draw board
        for x in range(0, 11):
            col.append(x * 10)
        for y in range(0, 11):
            row.append(y * 10)
        for x in col:
            ax_x = [x, x]
            ax_y = [row[0], row[10]]
            plt.plot(ax_x, ax_y, 'b.-', linewidth=0.5)
        for y in row:
            ax_x = [col[0], col[10]]
            ax_y = [y, y]
            plt.plot(ax_x, ax_y, 'b.-', linewidth=0.5)

        # Draw graph
        squares = [[0 for i in range(0)] for i in range(len(vertices_data))]
        vers_in_squares = [0] * len(vertices_data)
        for i in range(0, len(vertices_data)):
            square_num = vertices[i].get_square() - 1
            squares[square_num].append(i)
            vers_in_squares[square_num] += 1
        print(squares)
        print(vers_in_squares)

        for block in range(0, 100):
            x = []
            y = []
            if vers_in_squares[block] > 0:
                gap = 10.0 / (vers_in_squares[block] + 1)
                for i in range(0, vers_in_squares[block]):
                    x.append((block % 10) * 10 + gap * (i + 1))
                    y.append((10 - int(block / 10)) * 10 - gap * (i + 1))
                count = 0
                for vertex in squares[block]:
                    vertices[vertex].set_pos(x[count], y[count])
                    count += 1

        # Draw entire graph
        if entire is True:
            for vertex in vertices:
                x, y = vertex.get_pos()
                edges = vertex.get_connected_edge()
                plt.plot(x, y, 'go-')
                for dest in edges:
                    dest_x, dest_y = vertices[dest].get_pos()
                    line_x = [x, dest_x]
                    line_y = [y, dest_y]
                    plt.plot(line_x, line_y, 'go-', linewidth=0.5)



    return vertices

