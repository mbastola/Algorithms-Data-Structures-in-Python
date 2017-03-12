#Manil Bastola

import sys

#Helper function
def fibonacciMemoized(n, valList, k):
    '''returns nth value of k value fibonacci sequence'''
    if valList[n] >= 0:
        return valList[n]
    if n < 0:
        return 0
    else:
        acc = 0
        for i in range(1,k+1):
            acc = fibonacciMemoized(n-i, valList, k) + acc
        valList[n] = acc
        return valList[n]

#Wrapper    
def fibonacci(n,k):
    '''calls fibonaccimemoised and makes a list called valList to store values'''
    valList = [-1]*(n + 1)
    valList[0] = 0
    if n>0:
        valList[1] = 1
    return fibonacciMemoized(n, valList ,k)

def main():
    for i in range(0,21):
        print(fibonacci(i,int(sys.argv[1])))

main()
    
    
