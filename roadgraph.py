"""
Graph implementation in Python
"""

import logging

logger = logging.getLogger()


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        edges = []
        for vertex in self.graph_dict.keys():
            for neighbour in self.graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict.keys():
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        vertex_A, vertex_B = edge
        if vertex_A not in self.graph_dict.keys():
            self.graph_dict.update({vertex_A: [vertex_B]})
        else:
            self.graph_dict[vertex_A].append(vertex_B)
        if vertex_B not in self.graph_dict.keys():
            self.graph_dict.update({vertex_B: [vertex_A]})
        else:
            self.graph_dict[vertex_B].append(vertex_A)

    def find_path(self, start, end, path=None):
        if path is None:
            path = []
        else:
            path = list(path)
        path.append(start)
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        for vertex in self.graph_dict[start]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end, path)
                if extended_path:
                    return extended_path
        return None

    def find_paths(self, start, end, path=None):
        if path is None:
            path = []
        else:
            path = list(path)
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for vertex in self.graph_dict[start]:
            if vertex not in path:
                extended_paths = self.find_paths(vertex, end, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def bsf(self, vertex):
        queue = [vertex]
        visited = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
                for neighbour in self.graph_dict[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)

        return visited

    def __str__(self):
        return str(self.graph_dict)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(('a', 'b'))
    print(g)
    g.add_edge(('b', 'c'))
    print(g)
    g.add_edge(('c', 'd'))
    print(g)
    g.add_edge(('c', 'f'))
    print(g)
    g.add_edge(('f', 'g'))
    print(g)
    g.add_edge(('d', 'e'))
    print(g)
    g.add_edge(('a', 'e'))
    print(g)
    g.add_edge(('a', 'g'))
    print(g)
    print(g.find_paths('a', 'g', []))
    print('bsf', g.bsf('a'))
