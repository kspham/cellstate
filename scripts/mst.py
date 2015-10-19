__author__ = 'nadya'
import math

class Node:
    def __init__(self, i):
        self.parent = i
        self.rank = 1
        self.index = i
def find(nodes, i):
    if nodes[i].parent != i:
        nodes[i].parent = find(nodes, nodes[i].parent)
    return nodes[i].parent

def join(nodes, i, j):
    x = nodes[find(nodes, i)]
    y = nodes[find(nodes, j)]
    if x.index != y.index:
        if x.rank == y.rank:
            x.rank += 1
        if x.rank < y.rank:
            x.parent = y.index
        else:
            y.parent = x.index
    nodes[x.index] = x
    nodes[y.index] = y

def euclidean_distance(p1, p2):
    return math.sqrt(sum([(p1.coords[i] - p2.coords[i]) ** 2 for i in range(len(p1.coords))]))

def mst(points, distance):
    edges = []
    n = len(points)
    for i in range(n):
        for j in range((i + 1), n):
            edges.append((distance(points[i], points[j]), i, j))
    edges.sort()
    nodes = [Node(i) for i in range(n)]
    mst = []
    for (_, i, j) in edges:
        if find(nodes, i) != find(nodes, j):
            mst.append((i, j))
            join(nodes, i, j)
            if len(mst) == (n - 1):
                break
    return mst