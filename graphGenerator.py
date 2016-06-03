# Author: Josiah Bartlett & Tom Joyce
# Purpose: create a randomly weighted graph

from graph import Graph
from weightedgraph import WeightedGraph
import random
from itertools import combinations

class graphGenerator(Graph):

    def __init__(self, n, x, y):
        self.n = n # number of vertices in the graph
        self.x = x # lower bound for edge weight
        self.y = y # upper bound for edge weight
        self.vertexSet = set()
        for i in range(n):
            self.vertexSet.add(i)
        self.edgeList = list(combinations(self.vertexSet, 2))
        self.edgeweightSet = set()
        for m in self.edgeList:
            (a,b) = m
            self.edgeweightSet.add((a, b, random.randrange(self.x, self.y)))

        self.wgraph = WeightedGraph(self.vertexSet, self.edgeweightSet)