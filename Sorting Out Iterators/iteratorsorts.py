#Manil Bastola

from iterators import *
from linkedlist import *
from doublylinkedlist import *


def selectionSort(FAIter):
    while FAIter.getLoc() != None:
        #Find the min element in the part of the list
        curMin = FAIter.getItem()
        tmpIter = FAIter.clone()
        tmpIter.getNext()
        while tmpIter.getLoc()!= None:
            if tmpIter.getItem() < curMin:
                curMin = tmpIter.getItem()
                #Swap that min element with the element
                tmpIter.setItem(FAIter.getItem())
                FAIter.setItem(curMin)
            tmpIter.getNext()
        FAIter.getNext()

def insertionSort(BAIter):
    BAIter.getNext()
    while BAIter.getLoc() != None:
        tmpIter = BAIter.clone()
        valToInsert = tmpIter.getItem()
        newIter = tmpIter.clone()
        newIter.getPrevious()
        #Until we find the right place to put valToInsert...
        while newIter.getItem()!= None and newIter.getItem() > valToInsert:
            #Shift items over to make room
            tmpIter.setItem(newIter.getItem())
            tmpIter.getPrevious()
            newIter.getPrevious()
        #If we are here, currentPos must be the place
        tmpIter.setItem(valToInsert)
        BAIter.getNext()

###############################################################################          

def quickSort(startBAIter, endBAIter):
    first = startBAIter.clone()
    last = endBAIter.clone()
    quickSortHelper(first, last)

def quickSortHelper(first, last):
    if first.getLoc() < last.getLoc():
        #Arrange the list so everything before the split point
        #is less than the item at split point (and everything
        #after is greater than it)
        splitPoint = partition(first, last)

        #Sort the list to the left and to the right of splitpoint
        quickSortHelper(first, splitPoint.getPrevious())
        quickSortHelper(splitPoint.getNext(), last)

def partition(startBAIter, endBAIter):
    #Take the first item as the pivot value
    pivotVal = startBAIter.getItem()

    leftMark = startBAIter.clone().getNext()
    rightMark = endBAIter.clone()
    leftPos = leftMark.clone().getPrevious()
    rightPos = rightMark.clone().getNext()

    done = False
    while not done:
        #Move the leftMark until you find an item greater than the pivot
        while leftPos != rightMark.getLoc() and leftMark.getItem <= pivotVal:
            leftMark.getNext()

        #Move the rightMark until you find an item less than the pivot
        while rightMark.getLoc() >= leftMark.getLoc() and rightMark.getItem() >= pivotVal:
            rightMark.getPrevious()

        if rightMark.getLoc() < leftMark.getLoc():
            #If the left and right marks pass each other, 
            #we've looked at everything in the list
            done = True
        else:
            #If the left and right marks have not passed each other,
            #they are pointing at items that need to be swapped
            #so swap them
            tmp = leftMark.getItem()
            leftMark.setItem(rightMark.getItem)
            rightMark.setItem(tmp)

    #The right mark is now pointing at the last item in the list
    #that is less than pivotVal. Swap the first item with that item
    #and now the list is arrange appropriately.
    tmp = startBAIter.getItem()
    startBAIter.setItem(rightMark.getItem)
    rightMark.setIrem(tmp)

    return rightMark  
    
    



    

    

    
    

    
        
        
            
            
    
