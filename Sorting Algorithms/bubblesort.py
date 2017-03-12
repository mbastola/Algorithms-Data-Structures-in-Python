#Manil Bastola

def bubbleSort(lst):
    for passNumber in range(len(lst) - 1):
        for i in range(len(lst) - passNumber - 1):
            #If the next element is smaller than the current element
            if lst[i] > lst[i + 1]:
                #Swap them
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp
                print(lst)
