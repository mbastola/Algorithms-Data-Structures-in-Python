##Manil Bastola

from edgedatagraph import *
from queue import *
from minpriorityqueue import *
import sys

def createActorGraph(movieFilename):
    """Creates an EdgeDataGraph with actors as vertices where each actor is connected to every actor they've ever been in a movie with. The title of a shared movie is associated with the edge between every pair of actors."""
    myGraph = EdgeDataGraph()
    fin = open(movieFilename, 'r', encoding = "utf-8") 
    myLine = fin.readline()
    lineList = myLine.split(': ')
    data = lineList[1]
    myDict = {}
    while myLine != '':
        movie = lineList[1][:-1]
        myDict[movie] = []
        myLine = fin.readline()
        lineList = myLine.split(': ')
        while lineList[0] != 'Movie' and myLine != '':
            myDict[movie].append(lineList[-1][:-1])
            myLine = fin.readline()
            lineList = myLine.split(': ')
        for actor1 in myDict[movie]:
            for actor2 in myDict[movie]:
                if actor1 != actor2:
                    myGraph.addEdge(actor1, actor2, movie)
    fin.close()
    return myGraph
    
def findPath(graph, fromActor, toActor):
    """Returns a path using the shortest number of steps from fromActor to toActor."""
    vertexQueue = Queue()

    #The status dictionary will keep track of the status of each
    #vertex we consider
    #0 - Untouched
    #1 - Added to the queue
    status = {}
    vertices = graph.getVertices()
    for v in vertices:
        status[v] = 0

    #The path dictionary keeps track of the path from start vertex
    #to each other vertex. Specifically, for each vertex we store
    #the vertex that added it to the queue.
    path = {}

    vertexQueue.put(fromActor)
    status[fromActor] = 1
    
    while not vertexQueue.empty():
        vertex = vertexQueue.get()
        
        if vertex == toActor:
            #Regenerate the path
            pathList = [toActor]
            previousVertex = path.get(vertex, None)
            while previousVertex != None:
                pathList.append(previousVertex)
                previousVertex = path.get(previousVertex, None)
            pathList.reverse()
            return pathList

        neighbors = graph.getAdjacentVertices(vertex)        
        for n in neighbors:
            if status[n] == 0:
                vertexQueue.put(n)
                status[n] = 1
                path[n] = vertex

    #If we are here there is no path. Return None.
    return None

def findFamousPath(graph, fromActor, toActor, pathLength):
    """Returns the path from fromActor to toActor of length pathLength with the maximum sum of degrees of the vertices along the path."""
    visited = {}
    for item in graph.getVertices():
        visited[item] = False
    return findFamousPathHelper(graph, fromActor, toActor, pathLength, [], visited)[1] #calls helper function

def findFamousPathHelper(graph, fromActor, toActor, pathLength, curPath, visited):
    '''Helper function for findFamousPath that takes additional curPath and visited as parameters'''
    #Add a vertex to the current path.
    visited[fromActor] = True
    curPath.append(fromActor)
    #If the path is of the desired length and the current vertex is the target actor..
    if len(curPath) == pathLength and fromActor == toActor:
        copy = curPath[:]
        curPath.pop()
        visited[fromActor] = False
        sumDegree = 0
        for item in copy:
            sumDegree += len(graph.getAdjacentVertices(item))
        return (sumDegree, copy)
    #If the path is of the desired length but the current vertex is not the target actor..
    elif len(curPath) == pathLength and fromActor != toActor:
        curPath.pop()
        visited[fromActor] = False
        return (0, None)
    #Otherwise, recur to all as of yet unvisited neighbors..
    else:
        neighbors = graph.getAdjacentVertices(fromActor)
        sumDegree = len(neighbors)
        maxTuple = (0, None)
        for v in neighbors:
            if not visited[v]:
                newPath = findFamousPathHelper(graph, v , toActor, pathLength, curPath, visited)
                if newPath[0] > maxTuple[0]: #Return the path with the max sum of degrees.
                    maxTuple = newPath
        curPath.pop()
        visited[fromActor] = False
        return maxTuple
    
def getDistanceDistribution(graph, actor):
    """Returns a list where each element i contains the number of vertices i steps away from the given vertex."""
    vertexQueue = Queue()
    lst=[]
    #The status dictionary will keep track of the status of each
    #vertex we consider
    #0 - Untouched
    #1 - Added to the queue
    status = {}
    #The distance dictionary will keep track of the degree of separation with sourceVertex of each
    #vertex we consider 
    distance = {}
    vertices = graph.getVertices()
    for v in vertices:
        status[v] = 0
    distance[actor]=0
    vertexQueue.put(actor)
    status[actor] = 1
    while not vertexQueue.empty():
        vertex = vertexQueue.get()
        curPath = distance[vertex]
        if curPath >= len(lst):
            lst.append(0)
        lst[curPath]+= 1
        neighbors = graph.getAdjacentVertices(vertex)        
        for n in neighbors:
            if status[n] == 0:
                vertexQueue.put(n)
                newPath = distance[vertex]+1
                distance[n] = newPath
                status[n] = 1
    return lst
   
def findObscurePath(graph, fromActor, toActor):
    """Returns the path from fromActor to toActor that has the smallest sum of degrees amongst the vertices in the path."""
    vertices = graph.getVertices()

    distances = {}
    for v in vertices:
        #sys.maxsize is effectively infinity (bigger than all other numbers)
        distances[v] = sys.maxsize
    distances[fromActor] = 0
    
    pq = MinPriorityQueue()
    pq.enqueue(fromActor, 0)

    predecessors = {}
    predecessors[fromActor] = None

    while not pq.isEmpty():
        curVertex = pq.dequeue()
        neighbors = graph.getAdjacentVertices(curVertex)
        for n in neighbors:
            compareDist = distances[curVertex] + len(graph.getAdjacentVertices(n))
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
    return paths[toActor]

def actorInput(graph):
    """Keeps asking the user for a name until the name is in the database."""
    vertices = graph.getVertices()
    actor = input("Actor's name: ")
    while actor not in vertices:
        actor = input("Actor not in the database. Please select another: ")
    return actor

def printPath(graph, path):
    """Takes a path of actors and prints it out nicely."""
    for i in range(len(path) - 1):
        print(str(path[i]) + " and " + str(path[i + 1]) + " were in " + str(graph.getEdgeData(path[i], path[i + 1])))

def main():
    """Plays the Kevin Bacon game!"""
    print("Creating actor graph...")
    g = createActorGraph('top250.txt')
    
    center = "Kevin Bacon"
    quit = False
    while not quit:
        print("="*(len(center) + 19))
        print("Current center is: " + center)
        print("="*(len(center) + 19))
        print("s) Get statistics for the center")
        print("p) Find a path to another actor")
        print("f) Find a famous path to another actor")
        print("o) Find an obscure path to another actor")
        print("c) Change the center")
        print("q) Quit")

        userChoice = input("Please select an option: ")
        while userChoice not in ['p', 's', 'f', 'o', 'c', 'q']:
            print("Option not recognized, please type p, s, f, o, c, or q")
            userChoice = input("Please select an option: ")

        if userChoice == 'p':
            toActor = actorInput(g)
            path = findPath(g, center, toActor)
            if path == None:
                print("No path found!")
            else:
                print(str(toActor) + "'s " + center + " number is: " + str(len(path) - 1))
                printPath(g, path)
        elif userChoice == 's':
            distanceDistribution = getDistanceDistribution(g, center)
            sumDist = 0
            totalConnected = 0
            for i in range(len(distanceDistribution)):
                sumDist += i*distanceDistribution[i]
                totalConnected += distanceDistribution[i]
            print("Average distance: " + str(sumDist/totalConnected))
            print("Max distance: " + str(len(distanceDistribution) - 1))
            print("Percent connected: " + str(100*totalConnected/len(g.getVertices())))
        elif userChoice == 'f':
            toActor = actorInput(g)
            shortestPath = findPath(g, center, toActor)
            if shortestPath == None:
                print("No path found!")
            else:
                famousPath = findFamousPath(g, center, toActor, len(shortestPath))
                printPath(g, famousPath)
    
        elif userChoice == 'o':
            toActor = actorInput(g)
            obscurePath = findObscurePath(g, center, toActor)
            if obscurePath == None:
                print("No path found!")
            else:
                printPath(g, obscurePath)

        elif userChoice == 'c':
            center = actorInput(g)
        elif userChoice == 'q':
            quit = True
        input("(hit enter to continue)")

main()

########################################################################

