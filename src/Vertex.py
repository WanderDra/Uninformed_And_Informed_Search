

class Vertex:
    def __init__(self, num):
        self.empty = True
        self.num = 0
        self.connected_edge = []
        self.connected_distance = []
        self.num = num
        self.reached = False
        self.square = 0
        self.x = 0
        self.y = 0
        empty = False

    def add_edge(self, end, distance):
        if not self.connected_edge:
            self.connected_edge.append(end)
            self.connected_distance.append(distance)
        else:
            flag = False
            for i in range(0, len(self.connected_edge)):
                if distance < self.connected_distance[i]:
                    self.connected_edge.insert(i, end)
                    self.connected_distance.insert(i, distance)
                    flag = True
                    break
            if flag is False:
                self.connected_edge.append(end)
                self.connected_distance.append(distance)

    def get_distance_to(self, vertex_num):
        distance = -1
        i = 0
        for edge in self.connected_edge:
            if edge == vertex_num:
                distance = self.connected_distance[i]
            else:
                i += 1
        return distance

    def get_connected_edge(self):
        return self.connected_edge

    def get_connected_distance(self):
        return self.connected_distance

    def get_ver_num(self):
        return self.num

    def is_empty(self):
        return self.empty

    def is_reached(self):
        return self.reached

    def set_reached(self):
        self.reached = True

    def set_not_reached(self):
        self.reached = False

    def set_square(self, square):
        self.square = square

    def get_square(self):
        return self.square

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y
