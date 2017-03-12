#Manil Bastola

def selectionSort(lst):
    for posToFill in range(len(lst) - 1, 0, -1):
        #Find the position of the max element in the part of the list
        #from index 0 to posToFill
        maxPos = 0
        for pos in range(1, posToFill + 1):
            if lst[pos] > lst[maxPos]:
                maxPos = pos
        #Swap that max element with the element at posToFill
        tmp = lst[maxPos]
        lst[maxPos] = lst[posToFill]
        lst[posToFill] = tmp
        
