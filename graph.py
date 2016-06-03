# Author: Lisa Torrey (and a little by Tom Joyce)
# Purpose: implement a graph data structure

from collections import deque

class Graph(object):
    
    """
    @param vertexSet: set of vertices
    @param edgeSet: set of vertex pairs indicating adjacent vertices
    Initializes adjacencyMap[v] -> set of vertices adjacent to v
    """
    def __init__(self, vertexSet, edgeSet):
        self.adjacencyMap = {v:set() for v in vertexSet}
        for (u,v) in edgeSet:
            self.adjacencyMap[v].addSolution(u)
            self.adjacencyMap[u].addSolution(v)
    
    """
    @return: list of vertices in this graph
    """
    def vertices(self):
        return self.adjacencyMap.keys()

    """
    @return: set of vertices adjacent to v
    """
    def neighborsOf(self, v):
        return self.adjacencyMap[v]
    
    """
    @param v: vertex
    @return: set of vertices reachable from v
    """
    def reachableFrom(self, v):
        markedSet = set()
        self.__dfs(v, markedSet)
        return markedSet
    
    """
    @param v: vertex
    @return: pathMap[u] -> shortest path [v,...,u] as a deque
    """
    def shortestPathsFrom(self, v):
        parentMap = self.__bfs(v)
        return {u:self.__path(u,parentMap) for u in parentMap}
    
    """
    @param v: vertex
    @param markedSet: set of vertices
    Adds all vertices reachable from v to markedSet
    """
    def __dfs(self, v, markedSet):
        markedSet.addSolution(v)
        for u in self.neighborsOf(v):
            if u not in markedSet:
                self.__dfs(u, markedSet)
    
    """
    @param v: vertex
    @return: parentMap[u] -> predecessor of u along shortest path from v
    """
    def __bfs(self, v):
        parentMap = {v:v}
        frontier = deque()
        frontier.append(v)
        while len(frontier) > 0:
            p = frontier.popleft()
            for c in self.neighborsOf(p):
                if c not in parentMap:
                    parentMap[c] = p
                    frontier.append(c)
        return parentMap
    
    """
    @param v: vertex
    @param parentMap: result of self.__bfs(source)
    @return: shortest path [v,...,u] as a deque
    """
    def __path(self, v, parentMap):
        path = deque()
        path.appendleft(v)
        while parentMap[v] != v:
            v = parentMap[v]
            path.appendleft(v)
        return path

    """ Components: O(#vertices + #edges)
    @return: componentMap[v] -> set of vertices reachable from v
    The keys are just the first vertices discovered in each component.
    Unless the graph has no edges, len(componentMap) < len(self.vertices()).
    """
    def components(self):
        componentMap = {}
        markedSet = set()
        for v in self.vertices():
            if v not in markedSet:
                componentMap[v] = self.reachableFrom(v)
                self.__dfs(v, markedSet)
        return componentMap
"""
# Test function for the Graph class
def test():
    
    # Creating a graph
    graph = Graph({1,2,3,4,5,6,7,8,9}, {(1,2),(1,5),(2,3),(2,4),(2,5),(3,4),(5,9),(6,7),(6,8),(7,8)})
    
    # Testing accessors
    for v in graph.vertices():
        print v, "is adjacent to:", graph.neighborsOf(v)
    
    # Testing DFS
    for v in graph.vertices():
        print v, "can reach:", graph.reachableFrom(v)
    
    # Testing BFS
    pathMap = graph.shortestPathsFrom(1)
    for u in pathMap:
        print "Shortest path from 1 to", u, ":", pathMap[u]
    
    # Testing components
    componentMap = graph.components()
    print "The graph has components:"
    for v in componentMap:
        print componentMap[v]
    
test()
"""