from minpriorityqueue import *
import sys
from edgedatagraph import *

def dijkstra(graph, sourceVertex):
    """Takes a weighted graph and a vertex in that graph and performs Dijkstra's algorithm to find the shortest path from that vertex to all other vertices in the graph. Returns a dictionary of shortest paths, indexed by vertices"""
    vertices = graph.getVertices()

    distances = {}
    for v in vertices:
        #sys.maxsize is effectively infinity (bigger than all other numbers)
        distances[v] = sys.maxsize
    distances[sourceVertex] = 0
    
    pq = MinPriorityQueue()
    pq.enqueue(sourceVertex, 0)

    predecessors = {}
    predecessors[sourceVertex] = None

    while not pq.isEmpty():
        curVertex = pq.dequeue()
        neighbors = graph.getAdjacentVertices(curVertex)
        for n in neighbors:
            compareDist = distances[curVertex] + graph.getEdgeData(curVertex, n)
            if compareDist < distances[n]:
                predecessors[n] = curVertex
                if distances[n] == sys.maxsize:
                    #If the distance is infinite, this vertex is not
                    #on the PQ
                    pq.enqueue(n, compareDist)
                else:
                    #It is already on the PQ
                    pq.decreasePriority(n, distances[n], compareDist)
                distances[n] = compareDist

    paths = {}
    for v in vertices:
        if distances[v] < sys.maxsize:
            pathList = [v]
            previousVertex = predecessors[v]
            while previousVertex != None:
                pathList.append(previousVertex)
                previousVertex = predecessors[previousVertex]
            pathList.reverse()
            paths[v] = pathList
        else:
            paths[v] = None
    return paths

