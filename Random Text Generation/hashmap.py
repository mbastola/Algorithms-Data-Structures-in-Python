class HashMap:
    """Maps integer keys to arbitrary data items"""
    def __init__(self, size):
        """Creates an empty hash map with size initial slots."""
        self.keys = [None]*size
        self.data = [None]*size

    def store(self, key, dataItem):
        """Associates the given key with the given data and stores them. Key must be an integer."""
        hashValue = self.hash(key)
        
        if self.keys[hashValue] == None:
            #This slot is not taken -- store the key and data
            self.keys[hashValue] = key
            self.data[hashValue] = dataItem
        else:
            #This slot is taken
            found = False
            newHashVal = self.rehash(hashValue)
            
            #Find a new slot
            while not found and newHashVal != hashValue:
                if self.keys[newHashVal] == None:
                    found = True
                else:
                    newHashVal = self.rehash(newHashVal)

            #If newHashVal == hashValue, the table is full!
            if newHashVal == hashValue:
                print("Error: The table is full!")
                return
            else:
                #We found a slot
                self.keys[newHashVal] = key
                self.data[newHashVal] = dataItem

    def hash(self, item):
        """Converts a key to a slot index. Key must be an integer."""
        return item % len(self.keys)

    def rehash(self, hashVal):
        """Rehashes using linear probing, with step-size 1."""
        return (hashVal + 1) % len(self.keys)

    def search(self, key):
        """Returns the data item associated with the given key or none if the key is not in the table. Key must be an integer."""
        originalHashVal = self.hash(key)
        #If we find the key, return the data
        if self.keys[originalHashVal] == key:
            return self.data[originalHashVal]

        #Otherwise, we have to go looking, using rehashing
        hashVal = self.rehash(originalHashVal)
        while hashVal != originalHashVal:
            if self.keys[hashVal] == key:
                #We found the key. Return the data.
                return self.data[hashVal]
            elif self.keys[hashVal] == None:
                #We hit an empty slot. The key must not be in the table.
                return None
            else:
                hashVal = self.rehash(hashVal)
        #If we are here, we looped all the way around and couldn't find
        #the key. So it isn't here: return None.
        return None         

    def getKeyValuePairs(self):
        """Returns a list of tuples containing all key/data pairs in the table. The first element in the tuples returned is the key, the second element is the data."""
        keyValueList = []
        for i in range(len(self.keys)):
            if self.keys[i] != None:
                keyValueList.append((self.keys[i], self.data[i]))
        return keyValueList

    def __getitem__(self, key):
        """Overloads the [ ] operator -- allows indexing into the HashMap. Key must be an integer."""
        return self.search(key)

    def __setitem__(self, key, data):
        """Overloads the [ ] = operator -- allows assignment to entries of the HashMap. Key must be an integer."""
        self.store(key, data)

    def __str__(self):
        """Returns a string representation of the HashMap, including all the keys and associated data elements"""
        keyValues = self.getKeyValuePairs()
        dataStr = "HashMap{"
        #Add all but the last pair to the string
        #This way we can avoid having an extraneous ', ' on the end...
        for i in range(len(keyValues) - 1):
            dataStr += str(keyValues[i][0]) + ":" + str(keyValues[i][1]) + ", "

        if len(keyValues) == 0:
            #If the map is empty, just end the string
            return dataStr + "}"
        else:
            #Otherwise, add the last pair
            return dataStr + str(keyValues[-1][0]) + ":" + str(keyValues[-1][1]) + "}"

    def __repr__(self):
        """Returns a string representation of the HashMap for Python output. Gives the same string as __str__."""
        return str(self)

