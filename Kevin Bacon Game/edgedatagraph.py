from graph import *

class EdgeDataGraph(Graph):
    def __init__(self):
        super().__init__()

    def addVertex(self, vertex):
        """Add a vertex to the graph, associated with the given key (vertex)"""
        if vertex not in self.adjList:
            self.adjList[vertex] = {}
            
    def addEdge(self, vertex1, vertex2, data):
        """Add an edge from vertex1 to vertex2. Makes a tuple with vertex 2 and the data."""
        self.addVertex(vertex1)      
        self.addVertex(vertex2)

        if vertex2 not in self.adjList[vertex1]:
            self.adjList[vertex1][vertex2] = data

    def getEdgeData(self, vertex1, vertex2):
        '''Returns data associated with the vertices'''
        return self.adjList[vertex1][vertex2]

    def getEdges(self):
        """Returns a list of tuples representing edges in the graph. In each tuple the first element is the "from" vertex, the second is the "to" vertex"""
        edgeList = []
        for vertex in self.getVertices():
            for vertices in self.adjList[vertex]:
                edgeList.append((vertex, vertices))
        return edgeList


            
        
    
    
