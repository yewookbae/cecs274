from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""
class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def size(self):
        return self.n

    def add_edge(self, i : int, j : int):
        self.adj[i][j] = True

    def remove_edge(self, i : int, j : int) -> bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError("Vertex index out of range")
        if self.adj[i][j] == 1:
            self.adj[i][j] = 0
            self.adj[j][i] = 0
            return True
        else:
            return False

    def has_edge(self, i : int, j: int) ->bool:
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        edges = ArrayList.ArrayList()
        for j in range(self.n):
            if self.adj[i][j] == 1:
                edges.append(j)
        return edges

    def in_edges(self, i) -> List:
        edges = ArrayList.ArrayList()
        for j in range(self.n):
            if self.adj[j][i] == 1:
                edges.append(j)
        return edges

    def bfs(self, r : int):
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