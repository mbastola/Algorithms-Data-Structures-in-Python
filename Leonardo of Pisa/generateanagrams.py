#Manil Bastola

import sys

def Anagrams(myString):
    '''return the list of non repeating anagrams of the given myString'''
    myList = []
    if len(myString)==0:
        myList.append(myString)
        return myList
    else:
        for item in Anagrams(myString[1:]): #list of anagrams of shorter substring
            for i in range(0, len(item)+1):
                ana = item[:i] + myString[0] + item[i:] #adding the first letter of the string at each position
                if ana not in myList:
                    myList.append(ana)
        return myList

##def main():
##    for item in Anagrams(sys.argv[1]):
##        print(item)
##
##main()
    
                
            
    
    
