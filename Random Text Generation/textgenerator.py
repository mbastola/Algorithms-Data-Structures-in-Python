#Manil Bastola
#hw7

from chaininghashmap import *
import random

class TextGenerator:
    """A class that allows one to generate random text in the style of some provided source text"""
    def __init__(self):
        """Initializes the text generator"""
        self.countTable = ChainingHashMap(1000)
        self.totalTable = ChainingHashMap(1000)
        self.totalWords = 0

    def train(self, text):
        """Takes a body of text (as a string) and increases the appropriate frequency counts"""
        #Split the string into a list of words
        textList = text.split()
        #For each word (except the last one):

        for i in range(len(textList)-1):

        #Increase total words by 1

            self.totalWords += 1

        #Increase the count in totalTable associated with that word by 1
        #(or, if necessary, add the word and initialize its count)

            if self.totalTable[textList[i]] == None:
                self.totalTable[textList[i]] = 1
            else:
                self.totalTable[textList[i]] += 1

        #Increase the count in countTable associated with the word and the *next word* by 1
        #(or if necessary add the word and initialize its data to a new ChainingHashMap)
        #(if necesssary add the next word to the current word's hash map and initialize its count)
            if self.countTable[textList[i]] == None:
                self.countTable[textList[i]] = ChainingHashMap(1000)
            if self.countTable[textList[i]][textList[i+1]] == None:
                self.countTable[textList[i]][textList[i+1]] = 1
            else:
                self.countTable[textList[i]][textList[i+1]] +=  1


    def sampleWord(self, countList, totalCount):
        """Chooses a random string from a list, according to their relative frequencies. countList should be a list of tuples,
            where each tuple contains a string and a number (the frequency of that string). totalCount should be an integer,
            representing the total count of the words. Note: if the counts in countList do not add up to totalCount, trouble will ensue!"""
        randomNum = random.random()
        probabilitySum = 0
        for wordCount in countList:
            probabilitySum += wordCount[1]/totalCount
            if randomNum < probabilitySum:
                return wordCount[0]

    def generateText(self, numWords):
        """Using the frequency counts gathered in the train method, this method generates a random passage of text with numWords words."""
        #Generate the first word by sampling from totalTable (using totalWords as the total count)
        sample = self.sampleWord(self.totalTable.getKeyValuePairs(), self.totalWords)
        myText = '...' + sample 
        acc = 1
        #Until you have generated enough words:\
        #Generate the next word by sampling from the hash map in countTable indexed by
        #the previous word (using the number in totalTable indexed by the previous word as the total count)
        #Return the text with '...' added to the beginning and end
        
        while acc != numWords:
            sample = self.sampleWord(self.countTable[sample].getKeyValuePairs(), self.totalTable[sample])
            acc = acc+1
            myText += ' ' + sample
        return myText + '...'
    
#################################################################################################

class OrderKTextGenerator(TextGenerator):
    def __init__(self, order):
        super().__init__()
        self.order = order

    def train(self, text):
        """Takes a body of text (as a string) and increases the appropriate frequency counts"""
        #Split the string into a list of words
        textList = text.split()
        #For each word (except the last order):

        for i in range(len(textList)-self.order):

        #Increase total words by 1

            self.totalWords += 1
        #Create a string out of order words in the list, starting with this word (separated by spaces).
            word = textList[i]
            for j in range(1,self.order):
                word += ' ' + textList[i+j]
        #Increase the count in totalTable associated with that word by 1
        #(or, if necessary, add the word and initialize its count)

            if self.totalTable[word] == None:
                self.totalTable[word] = 1
            else:
                self.totalTable[word] += 1

        #Increase the count in countTable associated with the word and the *next word* by 1
        #(or if necessary add the word and initialize its data to a new ChainingHashMap)
        #(if necesssary add the next word to the current word's hash map and initialize its count)
            if self.countTable[word] == None:
                self.countTable[word] = ChainingHashMap(1000)
            if self.countTable[word][textList[i+self.order]] == None:
                self.countTable[word][textList[i+self.order]] = 1
            else:
                self.countTable[word][textList[i+self.order]] +=  1

    def generateText(self, numWords):
        """Using the frequency counts gathered in the train method, this method generates a random passage of text with numWords words."""
        #Generate a string of the first order words by using sampleWord to sample from totalTable.
        sample = self.sampleWord(self.totalTable.getKeyValuePairs(), self.totalWords)
        myText = '...' + sample 
        acc = 1
        #Until you have generated enough words:\
        #Generate the next word by sampling from the hash map in countTable indexed by
        #the previous word (using the number in totalTable indexed by the previous word as the total count)
        #Return the text with '...' added to the beginning and end
        
        while acc != numWords:
            sample = self.sampleWord(self.countTable[sample].getKeyValuePairs(), self.totalTable[sample])
            acc = acc+1
            myText += ' ' + sample
            newList = myText.split()
            newWord  = newList[-self.order]
            for i in range(-self.order + 1 , 0):
                newWord += ' '+ newList[i]
            sample = newWord
        return myText + '...'


        
    
            
        
