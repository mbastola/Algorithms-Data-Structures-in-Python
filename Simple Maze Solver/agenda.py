class Queue:
    def __init__(self):
        '''initializes the subclass Queue'''
        self.list = []
       
    def isEmpty(self):
        return len(self.list)==0

    def enqueue(self, item):
        self.list.insert(0,item)

    def dequeue(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def clear(self):
        self.list = []
    

    

    
                
        
