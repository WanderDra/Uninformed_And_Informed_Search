from Vertex import Vertex
from Readrer import read_data
import math
import copy
from matplotlib import pyplot as plt
import time


def astar(graph_name, end, start=0, draw=False, entire=False):
    vertices: Vertex
    vertices = read_data(graph_name, draw=draw, entire=entire)
    # Direction
    e_x, e_y = vertices[end].get_square_pos()
    open_list = []
    open_list.append(vertices[start])
    vertices[start].set_gx(0.0)
    h = [None] * len(vertices)
    f = [None] * len(vertices)
    s_x, s_y = vertices[start].get_square_pos()
    h[start] = int(math.sqrt(((e_x - s_x) * 10) ** 2 + ((e_y - s_y) * 10) ** 2)) / 2
    # h[start] = 0
    if h[start] < 0:
        h[start] = 0
    f[start] = vertices[start].get_gx() + h[start]
    temp_f = None
    # Searching
    calculation_times = 0
    while len(open_list) != 0:
        # print(len(open_list))
        v: Vertex
        v = open_list.pop()         # Current vertex
        v.set_closed()

        if v.get_ver_num() == end:
            temp_f = f[v.get_ver_num()]
            break

        connect_edges = v.get_connected_edge()
        connect_distances = v.get_connected_distance()
        # Set g(x) h(x) f(x) around v
        next_circle = False
        flag = False
        for vertex in range(0, len(connect_edges)):
            calculation_times += 1
            next_vertex: Vertex
            next_vertex = vertices[connect_edges[vertex]]
            if next_vertex.is_closed() is True:
                continue
            # g(x)
            predict_gx = connect_distances[vertex] + v.get_gx()
            if next_vertex.get_gx() is None:
                next_vertex.set_gx(predict_gx)
                next_vertex.set_back_pointer(v.get_ver_num())
            elif next_vertex.get_gx() > predict_gx:
                next_vertex.set_gx(predict_gx)
                next_vertex.set_back_pointer(v.get_ver_num())
                # Refresh possible
            # h(x)
            s_x, s_y = next_vertex.get_square_pos()
            h[next_vertex.get_ver_num()] = int(math.sqrt(((e_x - s_x) * 10) ** 2 + ((e_y - s_y) * 10) ** 2)) / 2
            # h[next_vertex.get_ver_num()] = 0
            if h[next_vertex.get_ver_num()] < 0:
                h[next_vertex.get_ver_num()] = 0
            # f(x)
            f[next_vertex.get_ver_num()] = next_vertex.get_gx() + h[next_vertex.get_ver_num()]

            if next_vertex.is_reached() is False:
                open_list.append(next_vertex)
                next_vertex.set_reached()

        # Put min_f vertex to the end of open_list
        f_min = None
        f_current = None
        f_min_pos = None
        f_min_open_list_pos = None
        count = 0
        if len(open_list) != 0:
            for ver in open_list:
                f_current = f[ver.get_ver_num()]
                if f_min is None or f_min > f_current:
                    f_min_pos = ver.get_ver_num()
                    f_min_open_list_pos = count
                    f_min = f_current
                count += 1

            open_list.append(vertices[f_min_pos])
            open_list.pop(f_min_open_list_pos)

    tracker = vertices[end].get_back_pointer()
    current_pos = vertices[end].get_pos()

    if temp_f is None:
        result = None
        print('Cannot reach the end')
    else:
        result = temp_f
        print('Result = ', result)

    print('Path = ')
    print(end)
    while tracker is not None:
        print('<-', tracker)
        tracker = vertices[tracker].get_back_pointer()
    tracker = vertices[end].get_back_pointer()

    print('Number of steps = ', calculation_times)

    # print(f)
    # print(h)

    # reach_list = []
    # for ver in vertices:
    #     reach_list.append(ver.is_reached())
    # print(reach_list)

    if draw:
        temp = vertices[end].get_ver_num()

        # print(end)
        result2 = 0
        while tracker is not None:
            # print(tracker)
            x, y = vertices[tracker].get_pos()
            x = [current_pos[0], x]
            y = [current_pos[1], y]
            plt.plot(x, y, 'r.-', linewidth=1)
            current_pos = vertices[tracker].get_pos()

            if tracker is not None:
                dis = vertices[tracker].get_connected_distance()
                result2 += dis[vertices[tracker].get_connected_edge().index(temp)]
            temp = tracker

            tracker = vertices[tracker].get_back_pointer()


        end_x, end_y = vertices[end].get_pos()
        plt.quiver(end_x, end_y - 10, 0, 1, color='r', width=0.005)

        # print(result2)

        plt.ioff()
        plt.show()

        # print(vertices[117].get_square_pos())
        # print(vertices[999].get_square_pos())

    return result



time_start = time.time()
astar('graph500_0.1', 83, start=0, draw=False, entire=False)
time_end = time.time()
print('Time cost = %fs' % (time_end - time_start))