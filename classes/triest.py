import random
from .edgestore import EdgeStore


class Triest:
    def __init__(self, filename, m):
        self.m = m
        self.filename = filename
        self.edge_store = EdgeStore()
        self.t1 = 0

    def flip_based_coin(self, t):
        head_prob = self.m / t
        coin = random.random()
        if coin < head_prob:
            return True
        else:
            return False

    def sample_edge_base(self, t):
        if t <= self.m:
            return True
        else:
            if self.flip_based_coin(t):
                edge_set = self.edge_store.get_edges()
                x, y = random.sample(edge_set, 1)[0]
                self.edge_store.remove_edge(x, y)
                self.update_counter_base("-", (x, y))
                return True
        return False

    def sample_edge_improved(self, t):
        if t <= self.m:
            return True
        else:
            if self.flip_based_coin(t):
                edge_set = self.edge_store.get_edges()
                x, y = random.sample(edge_set, 1)[0]
                self.edge_store.remove_edge(x, y)
                return True
        return False

    def update_counter_base(self, s, edge):
        x, y = edge
        vertices = self.edge_store.get_vertices()
        if x not in vertices or y not in vertices:
            return
        neighbourhood_x = self.edge_store.get_neighbours_set(x)
        neighbourhood_y = self.edge_store.get_neighbours_set(y)
        intersection = neighbourhood_x.intersection(neighbourhood_y)
        n = len(intersection)
        if s == '+':
            self.t1 += n
        else:
            self.t1 -= n

    def update_counter_improved(self, t, edge):
        x, y = edge
        vertices = self.edge_store.get_vertices()
        if x not in vertices or y not in vertices:
            return
        neighbourhood_x = self.edge_store.get_neighbours_set(x)
        neighbourhood_y = self.edge_store.get_neighbours_set(y)
        intersection = neighbourhood_x.intersection(neighbourhood_y)
        n = len(intersection)
        if n == 0:
            return
        w = (t - 1) * (t - 2) / (self.m * (self.m - 1))
        if w < 1:
            w = 1
        for _ in range(n):
            self.t1 += w

    def estimate_base(self, t):
        estimate = t * (t - 1) * (t - 2) / (self.m * (self.m - 1) * (self.m - 2))
        return int(estimate) * self.t1

    def run_triest_base(self):
        t = 0
        random.seed(1489)
        with open(self.filename) as f:
            for line in f:
                nodes = line.split()
                x = nodes[0]
                y = nodes[1]
                if x == y:
                    continue
                if x > y:
                    x, y = y, x
                if (x, y) in self.edge_store.get_edges():
                    continue
                t += 1
                if self.sample_edge_base(t):
                    self.edge_store.add_edge(x, y)
                    self.update_counter_base('+', (x, y))
        estimation = self.estimate_base(t)
        print(f'estimation = {estimation}')

    def run_triest_improved(self):
        t = 0
        random.seed(1489)
        with open(self.filename) as f:
            for line in f:
                nodes = line.split()
                x = nodes[0]
                y = nodes[1]
                if x == y:
                    continue
                if x > y:
                    x, y = y, x
                if (x, y) in self.edge_store.get_edges():
                    continue
                t += 1
                self.update_counter_improved(t, (x, y))
                if self.sample_edge_improved(t):
                    self.edge_store.add_edge(x, y)
        print(f'estimation = {int(self.t1)}')
