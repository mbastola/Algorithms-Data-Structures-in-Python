###################
## Manil Bastola
###################

from trie import *
import random

class WordSearch:
    """A class representing a word search game"""
    def __init__(self, width, height, wordListFilename):
        """Generates a random grid of letters of the given dimensions. Also initializes a dictionary using the given file (should be a list of words, one-per-line"""
        #Create a random grid of letters
        self.grid = []
        for r in range(height):
            self.grid.append([])
            for c in range(width):
                randomASCII = random.randint(ord('a'), ord('z'))
                self.grid[r].append(chr(randomASCII))

        #Construct the dictionary
        self.dict = Trie()
        fin = open(wordListFilename, 'r')
        for line in fin:
            word = line.split()
            self.dict.add(word[0])
        fin.close()
            
    def printGrid(self):
        """Prints the word search grid to the shell"""
        for r in range(len(self.grid)):
            rowStr = ''
            for c in range(len(self.grid[r])):
                rowStr += self.grid[r][c] + " "
            print(rowStr)

    def checkWord(self, word):
        """Returns True if the word is in the dictionary, False otherwise"""
        return self.dict.search(word)
        

    def verifyWord(self, word):
        """Returns True if the given string can be found on the grid (i.e. the word corresponds to a path of adjacent letters on the grid where no square is used twice)"""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                check = self.verifyWordMemo(i, j, word, 0) #calls recursive function
                if check == True:
                    return True
        return False
                    
    def verifyWordMemo(self, i, j, word, index):
        """Memoized Recursive function that takes current positions, word, and its index as parameter and recurses"""
        if self.grid[i][j] != word[index]:
            return False
        elif index >= len(word)-1:   #if we are at the end of the word, return true
            return True
        else:
            self.grid[i][j] = '#' #alters letter at that position in grid to '#'
            for row in range(-1,2):
                for col in range(-1,2):
                    if i + row < 0 or i + row > len(self.grid)-1:
                        row = 0
                    if j + col < 0 or j + col > len(self.grid[row])-1:
                        col = 0
                    check = self.verifyWordMemo(row + i, col + j , word, index+1) #recursive step
                    if check == True:
                        self.grid[i][j] = word[index] #changes '#' back to the letter
                        return True
                
    
    def findRemainingWords(self, wordsSoFar):
        """Takes a trie of words found so far. Returns the list of all words in the grid that are not in the trie. Note: this function modifies the given trie!"""
        finalRemWordList = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                finalRemWordList += self.findRemainingWordMemo('', i, j, wordsSoFar, [] ) #recursive step
        return finalRemWordList
            
    def findRemainingWordMemo(self,myStr, i,j, wordsSoFar, RemWordList):
        """Takes the string that has been constructed so far, the current position, the trie of previously
         found words, and a list of the remaining words found so far as parameters and preforms recursion """
        myStr = myStr + self.grid[i][j]
        if self.checkWord(myStr) and not wordsSoFar.search(myStr): #If the resulting string is in the dictionary and not previously found
            RemWordList.append(myStr)
            wordsSoFar.add(myStr)
            
        letter = self.grid[i][j]
        self.grid[i][j] ='#'  #change letter at that position in grid to '#'
        for row in range(-1,2):
            for col in range(-1,2):
                if i + row < 0 or i + row > len(self.grid)-1:
                    row = 0
                if j + col < 0 or j + col > len(self.grid[row])-1:
                    col = 0
                if self.grid[i+row][j+col] != '#' and self.dict.isPrefix(myStr):
                    self.findRemainingWordMemo(myStr, i+ row , j + col , wordsSoFar, RemWordList) #recursive step
        self.grid[i][j] = letter #changes '#' back to the letter
        return RemWordList

    

    

    
            
                    
                    
                    
        
            
