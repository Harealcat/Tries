class EdgeStore:
    def __init__(self):
        self.edges_neighbours = {}
        self.edges_set = set()

    def add_edge(self, a, b):
        if a in self.edges_neighbours.keys():
            self.edges_neighbours[a].add(b)
        else:
            self.edges_neighbours[a] = {b}
        if b in self.edges_neighbours.keys():
            self.edges_neighbours[b].add(a)
        else:
            self.edges_neighbours[b] = {a}
        self.edges_set.add((a, b))

    def remove_edge(self, a, b):
        self.edges_neighbours[a].remove(b)
        if len(self.edges_neighbours[a]) == 0:
            del self.edges_neighbours[a]
        self.edges_neighbours[b].remove(a)
        if len(self.edges_neighbours[b]) == 0:
            del self.edges_neighbours[b]
        self.edges_set.remove((a, b))

    def get_edges(self):
        return self.edges_set

    def get_neighbours_set(self, a):
        return self.edges_neighbours[a]

    def get_vertices(self):
        return self.edges_neighbours.keys()
