#Manil Bastola

def insertionSort(lst):
    for idxToInsert in range(1, len(lst)):
        valToInsert = lst[idxToInsert]
        currentPos = idxToInsert
        #Until we find the right place to put valToInsert...
        while currentPos > 0 and lst[currentPos - 1] > valToInsert:
            #Shift items over to make room
            lst[currentPos] = lst[currentPos - 1]
            currentPos = currentPos - 1
        #If we are here, currentPos must be the place
        lst[currentPos] = valToInsert
