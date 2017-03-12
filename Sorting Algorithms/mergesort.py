#Manil Bastola

def mergeSort(lst):
    if len(lst) > 1:
        #Split the list in half
        mid = len(lst)//2
        leftList = lst[:mid]
        rightList = lst[mid:]

        #Sort the two halves
        mergeSort(leftList)
        mergeSort(rightList)

        #Merge the sorted halves
        leftIndex = 0
        rightIndex = 0
        mergeIndex = 0
        #While there's something left in each of the left and the right
        while leftIndex < len(leftList) and rightIndex < len(rightList):
            if leftList[leftIndex] < rightList[rightIndex]:
                #If the current item from the left is smaller
                #than the current item from the right, put it
                #in the merged list
                lst[mergeIndex] = leftList[leftIndex]
                leftIndex += 1
            else:
                #Otherwise, put the one from the right in the merged list
                lst[mergeIndex] = rightList[rightIndex]
                rightIndex += 1

            mergeIndex += 1

        #If there's anything left from the left half
        #(if we ran out of stuff on the right), put it all in
        #the merged list
        while leftIndex < len(leftList):
            lst[mergeIndex] = leftList[leftIndex]
            leftIndex += 1
            mergeIndex += 1

        #Likewise the right (only one or the other of these loops will
        #actually occur)
        while rightIndex < len(rightList):
            lst[mergeIndex] = rightList[rightIndex]
            rightIndex += 1
            mergeIndex += 1
        
