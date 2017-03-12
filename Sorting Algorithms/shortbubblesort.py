#Manil Bastola

def shortBubbleSort(lst):
    for passNumber in range(len(lst) - 1):
        swapped = False
        for i in range(len(lst) - passNumber - 1):
            if lst[i] > lst[i + 1]:
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp
                swapped = True
                print(lst)
        #If we didn't make any swaps, the list must be sorted already
        if not swapped:
            return
