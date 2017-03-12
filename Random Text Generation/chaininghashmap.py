#Manil Bastola
# Hw7


from hashmap import *

class ChainingHashMap(HashMap):
    def __init__(self, size):
        '''initializes the subclass'''
        super().__init__(size)

    def store(self, key, dataItem):
        hashValue = self.hash(key)

        if self.keys[hashValue] == None:
            #This slot is not taken -- store the key and data
            self.keys[hashValue] = [key]
            self.data[hashValue] = [dataItem]
        else:
            found = False
            for i in range(len(self.keys[hashValue])):
                if self.keys[hashValue][i] == key:
                    self.data[hashValue][i] = dataItem
                    found = True
            if not found:
                self.keys[hashValue].append(key)
                self.data[hashValue].append(dataItem)
                
    def hash(self, item):
        '''converts the key to a string
and sums up the ASCII values of the characters in the string
and Returns the sum, modulo the number of slots in the table'''
        
        mystr = str(item)
        acc = 0
        for ch in mystr:
            acc = acc + ord(ch)
        return acc%len(self.keys)


    def search(self, key):
        '''searches for the key in the hashmap'''
        hashValue = self.hash(key)
        if self.keys[hashValue] == None:
            return None
        else:
            for i in range(len(self.keys[hashValue])):
                if self.keys[hashValue][i] == key:
                    return self.data[hashValue][i]
            return None

    def getKeyValuePairs(self):
        """Returns a list of tuples containing all key/data pairs in the table. The first element in the tuples returned is the key, the second element is the data."""
        keyValueList = []
        for i in range(len(self.keys)):
            if self.keys[i] != None:
                for j in range(len(self.keys[i])):
                    keyValueList.append((self.keys[i][j], self.data[i][j]))
        return keyValueList


        


    

    
                    
                    
            
            


        
                    
                    
        

    
                
            
                    
