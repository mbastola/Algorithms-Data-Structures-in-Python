#Manil Bastola

from iterators import *

class DoublyLinkedListNode:
    def __init__(self, item, next, prev):
        self.item = item
        self.next = next
        self.prev = prev

    def getItem(self):
        """Returns the data item"""
        return self.item

    def getNext(self):
        """Returns the next node"""
        return self.next

    def getPrevious(self):
        """Returns the preious node"""
        return self.prev

    def setItem(self, item):
        """Sets the data item"""
        self.item = item

    def setNext(self, next):
        """Sets the next node"""
        self.next = next

    def setPrevious(self, prev):
        """Sets the next node"""
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        """Creates an empty list"""
        self.head = None
        self.tail = None
        self.length = 0

    def getLength(self):
        """Returns the length of the list"""
        return self.length

    def isEmpty(self):
        """Returns True if the list is empty, False otherwise"""
        return self.length == 0

    def __str__(self):
        """Overloads the str operator. Returns a string representation of the list."""
        listStr = '['
        if self.isEmpty():
            listStr += ']'
        else:
            node = self.head
            for i in range(self.length - 1):
                listStr += str(node.getItem()) + " = "
                node = node.getNext()
            listStr += str(node.getItem()) + "]"
        return listStr

    def getReverseStr(self):
        '''Returns a string of the list in the reverse order'''
        listStr = '['
        if self.isEmpty():
            listStr += ']'
        else:
            node = self.tail
            for i in range(self.length - 1):
                listStr += str(node.getItem()) + " = "
                node = node.getPrevious()
            listStr += str(node.getItem()) + "]"
        return listStr

    def pushFront(self, item):
        """Adds a new item to the beginning of the list."""
        newNode = DoublyLinkedListNode(item, self.head , None)
        if self.isEmpty():
            self.tail = newNode
        else:
            self.head.setPrevious(newNode)
        self.head = newNode  
        self.length += 1

    def pushBack(self, item):
        """Adds a new item to the end of the list."""
        newNode = DoublyLinkedListNode(item, None , self.tail)
        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.setNext(newNode)
        self.tail = newNode
        self.length += 1

    def popFront(self):
        """Removes and returns an item from the beginning of the list"""
        if self.isEmpty():
            raise IndexError("Pop index out of bounds")
        item = self.head.getItem()
        self.head = self.head.getNext()
        self.length -= 1
        return item

    def popBack(self):
        """Removes and returns the item from the end of the list."""
        if self.isEmpty():
            raise IndexError("Pop index out of bounds")
        item = self.tail.getItem()
        self.tail = self.tail.getPrevious()
        self.length -= 1
        return item

    def getItem(self, index):
        """Returns the item at the given position. O(index)"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        node = self.head
        for i in range(index):
            node = node.getNext()
        return node.getItem()

    def setItem(self, index, item):
        """Sets the item at the given position. O(index)"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        node = self.head
        for i in range(index):
            node = node.getNext()
        return node.setItem(item)

    def search(self, item):
        """Returns True if the given item is in the list, False otherwise. O(n)"""
        #Just your basic sequential search...
        node = self.head
        for i in range(self.length):
            if node.getItem() == item:
                return True
            node = node.getNext()
        return False

    def __getitem__(self, index):
        """Overloads the [] operator. Returns the item at the given index."""
        return self.getItem(index)

    def __setitem__(self, index, item):
        """Overloads the []= operator. Sets the item at the given index."""
        self.setItem(index, item)

    def __len__(self):
        """Overloads the len operator. Returns the length of the list."""
        return self.getLength()

    def __contains__(self, item):
        """Overloads the in operator. Returns True if the item is in the list, False otherwise."""
        return self.search(item)

    def remove(self, index):
        '''Removes and returns the item at the given position.'''
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        elif index == self.length - 1:
            #In this case we're just removing the last element
            return self.popBack()
        elif index == 0:
            #In this case we're just removing the first element
            return self.popFront()
        else:
            #Otherwise, find the node *before* the one to remove
            previousNode = self.head
            for i in range(index - 1):
                previousNode = previousNode.getNext()
            #Its next node contains the item we are removing
            item = previousNode.getNext().getItem()
            #Re-wire the references to skip the removed node
            previousNode.setNext(previousNode.getNext().getNext())
            previousNode.setPrevious(self)
            self.length -= 1
            return item

    def insert(self, index, item):
        """Adds a new item at the given position. O(index)"""
        if index < 0:
            raise IndexError("Index out of bounds")
        elif index == 0:
            #In this case we're just adding to the front
            self.pushFront(item)
        elif index >= self.length:
            #For indices that are too large we follow the Python list convention
            #and just add to the back
            self.pushBack(item)
        else:
            #Otherwise, find the node *before* the given index
            previousNode = self.head
            for i in range(index - 1):
                previousNode = previousNode.getNext()
            #PreviousNode's next node is the node currently at the given index
            #It should be the new node's next
            newNode = DoublyLinkedListNode(item, previousNode.getNext(), self)
            #PreviousNode's next should be the new node
            previousNode.setNext(newNode)
            self.length += 1

    def getStartIter(self):
        """Returns a new iterator pointed at the beginning of the list."""
        return DoublyLinkedListBAIterator(self.head)
    
    def getEndIter(self):
        """Returns a new iterator pointed at the end of the list."""
        return DoublyLinkedListBAIterator(self.tail)

class DoublyLinkedListBAIterator(BidirectionalAssignableIterator):
    """An iterator for a doublylinked list structure."""
    def __init__(self, startNode):
        """Creates a new iterator pointed at the given node."""
        self.curNode = startNode

    def getNext(self):
        """Moves the iterator to the next position."""
        if self.curNode != None:
            self.curNode = self.curNode.getNext()
    
    def getPrevious(self):
        """Moves the iterator to the previous position."""
        if self.curNode != None:
            self.curNode = self.curNode.getPrevious()
            
    def getItem(self):
        """Returns the item at the iterator's current position."""
        if self.curNode != None:
            return self.curNode.getItem()
        else:
            return None
        
    def setItem(self,item):
        """Returns an object representing the iterator's current position.
         Returns None if the iterator has moved past the end of the collection."""
        if self.curNode != None:
            return self.curNode.setItem(item)

    def getLoc(self):
        """Returns the iterator's current node."""
        return self.curNode

    def clone(self):
        """Returns a new iterator pointed at the same node as this one."""
        return DoublyLinkedListBAIterator(self.curNode)
        
    












































