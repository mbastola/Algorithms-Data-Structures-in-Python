#Manil Bastola

class Queue:
    def __init__(self):
        '''initializes the class Queue'''
        self.list = []
       
    def isEmpty(self):
        return len(self.list)==0

    def enqueue(self,item):
        self.list.insert(0,item)

    def dequeue(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def clear(self):
        self.list = []

def radixSort(myList):
    queueList = []
    sortList =[]
    mainQueue = Queue()
    for i in range(0,10):
        queueList.append(Queue())
    maxItem = 0
    for item in myList:
        if maxItem < item:
            maxItem = item
        mainQueue.enqueue(str(item))
    for i in range(len(str(maxItem))-1,-1,-1):
        while not mainQueue.isEmpty():
            item = mainQueue.dequeue()   
            if len(item)<len(str(maxItem)):
                item = '0'*(len(str(maxItem))- len(item))+ item   
            queueList[int(item[i])].enqueue(item)
        for item in queueList:
            while not item.isEmpty():
                mainQueue.enqueue(item.dequeue())
    while not mainQueue.isEmpty():
        sortList.append(int(mainQueue.dequeue()))
    return sortList

########################################################################


    





        

    
            
        
        
        
        
    
    
