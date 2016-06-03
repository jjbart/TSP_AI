# Author: Lisa Torrey
# Purpose: implement an N-queens puzzle

import math
import random
from itertools import combinations
from graphGenerator import graphGenerator

class SimAnnealingTSPGraph(object):

    # @param graph: a weighted graph
    def __init__(self, graph):
        self.graph = graph
        self.pathlist = graph.vertices()

    # @return: a list of available moves
    # A move is a swap of two vertex indices, represented as a tuple
    def moves(self):
        return list(combinations(self.pathlist, 2))

    # @return: a copy of this graph
    def copy(self):
        copy = SimAnnealingTSPGraph(self.graph)
        for v in self.pathlist:
            copy.pathlist[v] = self.pathlist[v]

        return copy

    # @param move: an available move, represented as tuple of two indices
    # @return: a new graph with that move made
    def neighbor(self, moves):
        neighbor = self.copy()
        for move in moves:
            (v1,v2) = move
            temp = neighbor.pathlist[v1]
            neighbor.pathlist[v1] = neighbor.pathlist[v2]
            neighbor.pathlist[v2] = temp
        return neighbor

class SimAnnealingTSPAgent(object):

    # @param tspgraph: a weighted graph
    # @return: a weighted graph with its tour (pathlist) improved by simulated annealing
    def anneal(self, tspgraph):
        temp = 1.0 # initial temp
        random.shuffle(tspgraph.pathlist)
        while temp > 0.001: # almost zero
            count = 0
            moves = []
            while count <= len(tspgraph.pathlist)/50:
                moves.append(random.choice(tspgraph.moves()))
                moves.append(random.choice(tspgraph.moves()))
                count += 1
            neighbor = tspgraph.neighbor(moves)
            old_value, new_value = tspgraph.graph.pathlength(tspgraph.pathlist), neighbor.graph.pathlength(neighbor.pathlist)
            if new_value <= old_value:
                tspgraph = neighbor
                diff = (new_value - old_value)  # must be negative
                p = math.exp(diff/temp)
                if random.random() < p: # with probability p
                    tspgraph = neighbor
            temp *= 0.999 # decay
        return tspgraph
