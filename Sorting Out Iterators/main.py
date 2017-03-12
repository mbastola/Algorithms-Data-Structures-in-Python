#Manil Bastola

from iterators import *
from linkedlist import *
from iteratorsorts import *
from doublylinkedlist import *
import random

def main():
    PylistCollection = [] #creates list to store lists
    LinkedListCollection = []
    
    for i in range(10):
        alist = []
        blist = LinkedList()
        for j in range(20):
            alist.append(random.randint(0,50))
            blist.pushBack(random.randint(0,50))
        PylistCollection.append(alist) #adds python lists to PyListCollection for selectionSort
        LinkedListCollection.append(blist) # adds linked lists to LinkedListCollection for selectionSort

    PylistCollection.append([random.randint(1,10)])
    PylistCollection.append([])
    new = LinkedList()
    new.pushBack(random.randint(1,10))
    LinkedListCollection.append(new)
    null = LinkedList()
    LinkedListCollection.append(null)
    

    for item in PylistCollection:
        print('Python List = ',item)
        selectionSort(PythonListFAIterator(item, 0))
        print('After Selection Sorting =', item, '\n' )

    for item in LinkedListCollection:
        print('Linked List = ',item,)
        selectionSort(item.getStartIter())
        print('After Selection Sorting =', item , '\n')

    newPylistCollection = []
    DoublyLinkedListCollection = []

    for i in range(10):
        newalist = []
        BiDirectionalList = DoublyLinkedList()
        for j in range(20):
            newalist.append(random.randint(0,50))
            BiDirectionalList.pushFront(random.randint(0,50))
        newPylistCollection.append(newalist) #adds python lists to PyListCollection for insertionSort
        DoublyLinkedListCollection.append(BiDirectionalList) #adds python lists to DoublyLinkedListCollection for insertionSort
    

    newPylistCollection.append([random.randint(1,10)])
    newPylistCollection.append([])
    DoublyLinkedListCollection.append(DoublyLinkedList())
    alist = DoublyLinkedList()
    alist.pushFront(random.randint(0,10))
    DoublyLinkedListCollection.append(alist)
    
    for item in newPylistCollection:
        print('Python List = ',item)
        insertionSort(PythonListBAIterator(item, 0))
        print('After Insertion Sorting =', item, '\n' )

    for item in DoublyLinkedListCollection:
        print('DoublyLinked List = ',item)
        insertionSort(item.getStartIter())
        print('After Insertion Sorting =', item, '\n' )

main()

    
