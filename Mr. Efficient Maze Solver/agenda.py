####################
## Manil Bastola
####################

import abc
from linkedlist import *
from minpriorityqueue import *

class Agenda(metaclass=abc.ABCMeta):
    """An abstract class providing the interface for an agenda which stores and returns items in a specific order"""
    @abc.abstractmethod
    def addItem(self, item, pathLength):
        """Add an item to the agenda"""
        return

    @abc.abstractmethod
    def getItem(self):
        """Return and remove the next item from the agenda"""
        return

    @abc.abstractmethod
    def isEmpty(self):
        """Returns True if the agenda is empty, False otherwise"""
        return

    @abc.abstractmethod
    def clear(self):
        """Makes the agenda empty"""
        return

class StackAgenda(Agenda):
    """An agenda that acts like a stack -- returning items in FILO order."""
    def __init__(self):
        """Create an empty agenda"""
        self.__data = LinkedList()

    def addItem(self, item, pathLength):
        """Add an item to the agenda"""
        self.__data.pushFront(item)

    def getItem(self):
        """Return and remove the next item from the agenda"""
        return self.__data.popFront()

    def isEmpty(self):
        """Returns True if the agenda is empty, False otherwise"""
        return self.__data.isEmpty()

    def clear(self):
        """Makes the agenda empty"""
        self.__data = LinkedList()

class QueueAgenda(Agenda):
    """An agenda that acts like a queue -- returning items in a FIFO order."""
    def __init__(self):
        """Creates an empty agenda"""
        self.__data = LinkedList()

    def addItem(self, item, pathLength):
        """Add an item to the agenda"""
        self.__data.pushBack(item)

    def getItem(self):
        """Return and remove the next item from the agenda"""
        return self.__data.popFront()

    def isEmpty(self):
        """Returns True if the agenda is empty, False otherwise"""
        return self.__data.isEmpty()

    def clear(self):
        """Makes the agenda empty"""
        self.__data = LinkedList()

class Evaluator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def evaluateItem(self,item):
        '''Takes an item and returns a numeric score for that item.'''
        return

class PriorityQueueAgenda(Agenda):
    def __init__(self, evaluator):
        """Creates an empty agenda and stores evaluator object as instance variable"""
        self.evaluator = evaluator
        self.__data = MinPriorityQueue([])

    def addItem(self, item, pathLength):
        """Add an item to the agenda"""
        self.__data.enqueue(item,self.evaluator.evaluateItem(item))

    def getItem(self):
        """Return and remove the next item from the agenda"""
        return self.__data.dequeue()

    def isEmpty(self):
        """Returns True if the agenda is empty, False otherwise"""
        return self.__data.isEmpty()

    def clear(self):
        """Makes the agenda empty"""
        self.__data = MinPriorityQueue()

class ManhattanDistanceEvaluator(Evaluator):
    def __init__(self, goalLoc ):
        super().__init__()
        self.row = goalLoc[0]
        self.col = goalLoc[1]

    def evaluateItem(self,item):
        return abs(self.row - item[0]) + abs(self.col - item[1])

class AStarAgenda(Agenda):
    
    def __init__(self, evaluator):
        """Creates an empty agenda and stores evaluator object as instance variable"""
        self.evaluator = evaluator
        self.__data = MinPriorityQueue([])

    def addItem(self, item, pathLength):
        """Add an item to the agenda"""
        self.__data.enqueue(item,self.evaluator.evaluateItem(item) + pathLength)

    def getItem(self):
        """Return and remove the next item from the agenda"""
        return self.__data.dequeue()

    def isEmpty(self):
        """Returns True if the agenda is empty, False otherwise"""
        return self.__data.isEmpty()

    def clear(self):
        """Makes the agenda empty"""
        self.__data = MinPriorityQueue()
        
    

    
        
