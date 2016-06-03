# Author: Lisa Torrey (and a little by Tom Joyce and Josiah Bartlett)
# Purpose: implement a weighted graph data structure

from graph import Graph
from heapq import *

class WeightedGraph(Graph):

    """
    @param vertexSet: set of vertices
    @param edgeSet: set of (v,u,weight) tuples indicating edges
    Initializes adjacencyMap[v][u] -> weight of edge v->u
    """
    def __init__(self, vertexSet, edgeSet):
        self.adjacencyMap = {v:dict() for v in vertexSet}
        for (v,u,weight) in edgeSet:
            self.adjacencyMap[v][u] = weight
            self.adjacencyMap[u][v] = weight
    
    """
    @params v,u: vertices
    @return: weight of edge v->u
    """
    def edgeWeight(self, v, u):
        return self.adjacencyMap[v][u]

    """
    @param v: vertex
    @return: pathMap[u] -> minimum-weight path [v,...,u] as a deque
    """
    def shortestPathsFrom(self, v):
        parentMap = self.__dijkstra(v)
        return {u:self._Graph__path(u,parentMap) for u in parentMap}
    
    """
    @param v: vertex
    @return: parentMap[u] -> predecessor of u along minimum-weight path from v
    """
    def __dijkstra(self, v):
        parentMap = {v:v}
        distanceMap = {v:0}
        frontier = [(0,v)]
        ignoreSet = set()
        while len(frontier) > 0:
            (pdist,p) = heappop(frontier)
            if p not in ignoreSet:
                ignoreSet.add(p)
                for c in self.neighborsOf(p):
                    d = pdist + self.edgeWeight(p,c)
                    if c not in parentMap or distanceMap[c] > d:
                        parentMap[c] = p
                        distanceMap[c] = d
                        heappush(frontier, (d,c))
        return parentMap

    """
    authors: Josiah Bartlett and Tom Joyce
    @param v: start/end vertex
    @return: minimum weight TSP tour list and length
    """
    def greedytsp(self, v):
        sum = 0
        start = v
        markedvertices = [v]
        vertexlist = self.vertices()
        while len(markedvertices) < len(vertexlist):
            weightdict = {}
            for i in self.neighborsOf(v):
                if i not in markedvertices:
                    weight = self.edgeWeight(v, i)
                    weightdict[i] = weight
            if len(weightdict) > 0:
                v = min(weightdict, key=lambda k: weightdict[k])
                sum = sum + weightdict[v]
                markedvertices.append(v)

        sum = sum + self.edgeWeight(v, start)
        return (markedvertices, sum)

    """
    authors: Josiah Bartlett and Tom Joyce
    @param v: start/end vertex
    @return: minimum weight TSP tour list and length
    """
    def pathlength(self, pathlist):
        length = 0
        i = 0
        if len(pathlist) > 1:
            while i < (len(self.vertices()))-1:
                v1 = pathlist[i]
                v2 = pathlist[i + 1]
                length += self.edgeWeight(v1, v2)
                i+=1
            length += self.edgeWeight(v2, pathlist[0])
        return length

    """
    @param a: start vertex
    @param b: end vertex
    @param c: a required vertex
    @return: the cheapest path [a...b] that passes through c
    """
    def pathThrough(self,a,b,c):
        pathMapA = self.shortestPathsFrom(a)
        pathMapC = self.shortestPathsFrom(c)
        
        for v in pathMapC(b):
            pathMapA[c].append(v)
        
        return pathMapA
         
        
    """
    @param a: start vertex
    @param b: end vertex
    @param c: a restricted vertex 
    @return: the cheapest path [a...b] that does not pass through c
    """
    def pathNotThrough(self,a,b,c):
        
        subVertexSet = []
        subEdgeSet = []
        
        for v in self.vertexSet:
            if v != c:
                subvertexSet.addSolution(c)
        
        for weight in self.adjacencyMap:
            if weight != adjacencyMap[v][c]:
                subEdgeSet.add(v, u, weight)
        
        subgraph = WeightedGraph(subVertexSet, subEdgeSet)
        
        pathMap = subgraph.shortestPathsFrom(a)
        return pathMap[b]
"""
# Test function for the WeightedGraph class
def test():
    
    # Creating a graph
    graph = WeightedGraph({'A','B','C','D','E'},{('A','B',4),('A','C',2),('B','C',1),('B','D',3),('C','E',6),('D','E',1)})
    graph2 = WeightedGraph({'A', 'B', 'C', 'D', 'E', 'F', 'G'}, {('A','B',7),('A','D',5),('A','C',9),('B','C',4),('B','E',5),('B','F',2),('E','F',2),('C','D',7),('C','G',4),('G','F',7),('C','F',3),('D','G',12)})
    
    # Testing Dijkstra
    pathMap = graph.shortestPathsFrom('A')
    pathMap2 = graph2.shortestPathsFrom('A')
    for v in pathMap:
        print "Minimum-weight path from 1 to", v, ":", pathMap[v]
    for v in pathMap2:
        print "Minimum-weight path from 1 to", v, ":", pathMap2[v]
    
    path1 = graph2.pathThrough('A','F','C')
    print path1
    
    path2 = graph2.pathNotThrough('A','F','B')
    print path2
test()
"""