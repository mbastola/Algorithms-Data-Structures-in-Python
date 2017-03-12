#Manil Bastola

from iterators import *

class LinkedListNode:
    """Represents a single node in a linked list"""
    def __init__(self, item, next):
        """Takes a data item and the next node for this node to point to (or None)"""
        self.item = item
        self.next = next

    def getItem(self):
        """Returns the data item"""
        return self.item

    def getNext(self):
        """Returns the next node"""
        return self.next

    def setItem(self, item):
        """Sets the data item"""
        self.item = item

    def setNext(self, next):
        """Sets the next node"""
        self.next = next

class LinkedList:
    """A class representing a linked list structure"""
    def __init__(self):
        """Creates an empty list"""
        self.head = None
        self.length = 0

    def getLength(self):
        """Returns the length of the list"""
        return self.length

    def isEmpty(self):
        """Returns True if the list is empty, False otherwise"""
        return self.length == 0

    def pushFront(self, item):
        """Adds a new item to the beginning of the list. O(1)"""
        newNode = LinkedListNode(item, self.head)
        self.head = newNode
        self.length += 1

    def popFront(self):
        """Removes and returns an item from the beginning of the list. O(1)"""
        if self.isEmpty():
            raise IndexError("Pop index out of bounds")

        item = self.head.getItem()
        self.head = self.head.getNext()
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

    def remove(self, index):
        """Removes and returns the item at the given position. O(index)"""
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
            self.length -= 1
            return item

    def setItem(self, index, item):
        """Sets the item at the given position. O(index)"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        node = self.head
        for i in range(index):
            node = node.getNext()
        return node.setItem(item)

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
            newNode = LinkedListNode(item, previousNode.getNext())
            #PreviousNode's next should be the new node
            previousNode.setNext(newNode)
            self.length += 1

    def pushBack(self, item):
        """Adds an item to the end of the list. O(n)"""
        if self.isEmpty():
            #If the list is empty, this is the same as pushFront
            self.pushFront(item)
        else:
            #Find the last node
            node = self.head
            for i in range(self.length - 1):
                node = node.getNext()
            #Make the new node the next of the last node
            newNode = LinkedListNode(item, None)
            node.setNext(newNode)
            self.length += 1

    def popBack(self):
        """Removes and returns the item from the end of the list. O(n)"""
        if self.isEmpty():
            raise IndexError("Pop index out of bounds")
        elif self.length == 1:
            #If the list has only one element, popBack is the same as popFront
            return self.popFront()
        else:
            #Find the node *before* the last node
            previousNode = self.head
            for i in range(self.length - 2):
                previousNode = previousNode.getNext()
            #PreviousNode's next is the last node, so get its item
            item = previousNode.getNext().getItem()
            #Make previousNode the last node by setting its next to None
            previousNode.setNext(None)
            self.length -= 1
            return item

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

    def __str__(self):
        """Overloads the str operator. Returns a string representation of the list."""
        listStr = '['
        if self.isEmpty():
            listStr += ']'
        else:
            node = self.head
            for i in range(self.length - 1):
                listStr += str(node.getItem()) + " > "
                node = node.getNext()
            listStr += str(node.getItem()) + "]"
        return listStr        

    def getStartIter(self):
        """Returns a new iterator pointed at the beginning of the list."""
        return LinkedListFAIIterator(self.head)

    def __iter__(self):
        """Provides for loop funcionality. Returns a new iterator pointed at the beginning of the list."""
        return self.getStartIter()

class LinkedListIterator(ForwardIterator):
    """An iterator for a linked list structure."""
    def __init__(self, startNode):
        """Creates a new iterator pointed at the given node."""
        self.curNode = startNode

    def getNext(self):
        """Moves the iterator to the next position."""
        if self.curNode != None:
            self.curNode = self.curNode.getNext()

    def getItem(self):
        """Returns the item at the iterator's current position."""
        if self.curNode != None:
            return self.curNode.getItem()
        else:
            return None

    def getLoc(self):
        """Returns the iterator's current node."""
        return self.curNode

    def clone(self):
        """Returns a new iterator pointed at the same node as this one."""
        return LinkedListIterator(self.curNode)

######################################################################

class LinkedListFAIIterator(ForwardAssignableIterator):
    def __init__(self, startNode):
        self.curNode = startNode

    def getNext(self):
        """Moves the iterator to the next position."""
        if self.curNode != None:
            self.curNode = self.curNode.getNext()

    def getItem(self):
        if self.curNode != None:
            return self.curNode.getItem()
        else:
            return None

    def setItem(self, item):
        if self.curNode != None:
            return self.curNode.setItem(item)

    def getLoc(self):
        return self.curNode

    def clone(self):
        return LinkedListFAIIterator(self.curNode)
        
        
        

    

        
        
    
