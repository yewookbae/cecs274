"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def size(self):
        return self.n

    def add_edge(self, i : int, j : int):
        # todo
        if not self.has_edge(i, j):
            self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        # todo
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        # todo
        return self.adj[i]

    def in_edges(self, i) -> List:
        # todo
        edges = []
        for j in range(self.n):
            if self.has_edge(j, i):
                edges.append(j)
        return edges

    def bfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        seen = [False for k in range(self.n)]
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while q.n > 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for j in neighbors:
                if seen[j] is False:
                    q.add(j)
                    traversal.append(j)
                    seen[j] = True
        return traversal

    def dfs(self, r : int):
        # todo
        a1 = ArrayList.ArrayList()
        a2 = ArrayStack.ArrayStack()
        i = [False for k in range(self.n)]
        a2.push(r)
        while a2.n > 0:
            l = a2.pop()
            if i[l] is False:
                a1.append(l)
                i[l] = True
            horse = reversed(self.out_edges(l))
            for table in horse:
                if i[table] is False:
                    a2.push(table)
        return a1

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
