#Manil Bastola

def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if first < last:
        #Arrange the list so everything before the split point
        #is less than the item at split point (and everything
        #after is greater than it)
        splitPoint = partition(lst, first, last)

        #Sort the list to the left and to the right of splitpoint
        quickSortHelper(lst, first, splitPoint - 1)
        quickSortHelper(lst, splitPoint + 1, last)

def partition(lst, first, last):
    #Take the first item as the pivot value
    pivotVal = lst[first]

    leftMark = first + 1
    rightMark = last

    done = False
    while not done:
        #Move the leftMark until you find an item greater than the pivot
        while leftMark <= rightMark and lst[leftMark] <= pivotVal:
            leftMark = leftMark + 1

        #Move the rightMark until you find an item less than the pivot
        while rightMark >= leftMark and lst[rightMark] >= pivotVal:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            #If the left and right marks pass each other, 
            #we've looked at everything in the list
            done = True
        else:
            #If the left and right marks have not passed each other,
            #they are pointing at items that need to be swapped
            #so swap them
            tmp = lst[leftMark]
            lst[leftMark] = lst[rightMark]
            lst[rightMark] = tmp

    #The right mark is now pointing at the last item in the list
    #that is less than pivotVal. Swap the first item with that item
    #and now the list is arrange appropriately.
    tmp = lst[first]
    lst[first] = lst[rightMark]
    lst[rightMark] = tmp

    return rightMark
