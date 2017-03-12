#Manil Bastola

from abc import *

class ForwardIterator(metaclass=ABCMeta):
    """Provides the interface for a forward, read-only iterator."""
    @abstractmethod
    def getNext(self):
        """Moves the iterator to the next position"""
        return

    @abstractmethod
    def getItem(self):
        """Returns the item at the current position"""
        return

    @abstractmethod
    def getLoc(self):
        """Returns an object representing the iterator's current position (the type of this object may be specific to the container being iterated over). Returns None if the iterator has moved past the end of the collection."""
        return

    @abstractmethod
    def clone(self):
        """Return a new iterator pointing to the same location as this one"""
        return

    def __eq__(self, other):
        """Overloads the == operator. Returns True if the two iterators are pointing to the same location, False otherwise."""
        return self.getLoc() == other.getLoc()
    
    def __ne__(self, other):
        """Overloads the != operator. Returns the opposite of __eq__"""
        return not (self == other)

    def __next__(self):
        """Provides for loop funcionality. Returns the current item and moves the iterator to the next position. Raises StopIteration if the iterator has moved off of the collection."""
        if self.getLoc() == None:
            raise StopIteration
        else:
            item = self.getItem()
            self.getNext()
            return item

class ForwardAssignableIterator(ForwardIterator):

    @abstractmethod
    def setItem(self,item):
        '''Sets the item at the current position.'''
        return
###################################################################################

class PythonListFAIterator(ForwardAssignableIterator):
    def __init__(self, lst, index):
        self.list = lst
        self.index = index
        
    def getNext(self):
        """Moves the iterator to the next position"""
        self.index += 1

    def getItem(self):
        """Returns the item at the current position"""
        if self.index <= len(self.list)-1:
            return self.list[self.index]
        else:
            return None

    def setItem(self,item):
        """Returns an object representing the iterator's current position.
         Returns None if the iterator has moved past the end of the collection."""
        if self.index <= len(self.list)-1:
            self.list[self.index] = item

    def getLoc(self):
        """Returns an object representing the iterator's current position.
        Returns None if the iterator has moved past the end of the collection."""
        if self.index <= len(self.list)-1:
            return self.index

    def clone(self):
        """Return a new iterator pointing to the same location as this one"""
        return PythonListFAIterator(self.list, self.index)

##############################################################################

class BidirectionalAssignableIterator(ForwardAssignableIterator):

    @abstractmethod
    def getPrevious(self):
        '''Moves the iterator to the previous location in the collection.'''
        return

class PythonListBAIterator(BidirectionalAssignableIterator):
    def __init__(self, lst, index):
        self.list = lst
        self.index = index
        
    def getNext(self):
        """Moves the iterator to the next position"""
        self.index += 1

    def getItem(self):
        """Returns the item at the current position"""
        if 0 <= self.index <= len(self.list)-1:
            return self.list[self.index]
        else:
            return None

    def setItem(self,item):
        """Returns an object representing the iterator's current position.
         Returns None if the iterator has moved past the end of the collection."""
        if self.index <= len(self.list)-1:
            self.list[self.index] = item

    def getLoc(self):
        """Returns an object representing the iterator's current position.
        Returns None if the iterator has moved past the end of the collection."""
        if self.index <= len(self.list)-1:
            return self.index

    def clone(self):
        """Return a new iterator pointing to the same location as this one"""
        return PythonListBAIterator(self.list, self.index)

    def getPrevious(self):
        '''Moves the iterator to the previous location in the collection.'''
        self.index -= 1
        
    
    
    
        
        
        

    
        
        
        
    

        
        
    
