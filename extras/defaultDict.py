#!/usr/bin/python3
from collections import defaultdict

class Graph:
    def __init__(self,edges):
        self.routes = edges
        self.route_dict = defaultdict(list)
        self.visited = []
        for start, end in self.routes:
            self.route_dict[start].append(end)


    def get_paths(self, start, end, path=[]):
        path += [start]
        if start == end:
            return path
        if not self.route_dict.get(start):
            return []
        paths = []
        for node in self.route_dict.get(start):
            self.visited.append(self.get_paths(node, end, path))
            path = [start]


    def get_routes(self):
        return self.route_dict

    def get_path(self):
        return self.visited




if __name__ == '__main__':
    routes = [('Mumbai', 'Paris'), ('Mumbai', 'Dubai'), ('Paris', 'Dubai'), ('Paris', 'New york'), ('Dubai', 'New york'), ('New york', 'Toronto')]
    graph = Graph(routes)
    start = "Mumbai"
    end = "Dubai"
    graph.get_paths(start, end)
    print(graph.get_routes())
    print(graph.get_path())

