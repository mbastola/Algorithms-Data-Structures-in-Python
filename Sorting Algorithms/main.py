from mysterysorts import *
import random
import time

print(sort1)
sort1([45,20,6,15,30,47,78,13])

print(sort2)
sort2([45,20,6,15,30,47,78,13])
print(sort3)
sort3([45,20,6,15,30,47,78,13])
print(sort4)
sort4([45,20,6,15,30,47,78,13])
print(sort5)
sort5([45,20,6,15,30,47,78,13])
print(sort6)
sort6([45,20,6,15,30,47,78,13])

##def test():
##    for n in range(1000,11000,1000):
##        avgTime1 = 0 #average running time 
##        avgTime2 = 0
##        avgTime3 = 0
##        avgTime4 = 0
##        avgTime5 = 0
##        avgTime6 = 0
##
##        for i in range(100):
##            myList = []
##            for j in range(n):
##                myList.append(random.randint(0,n))
##
##
##            myList1 = myList[:]
##            myList2 = myList[:]
##            myList3 = myList[:]
##            myList4 = myList[:]
##            myList5 = myList[:]
##                
##            startTime = time.time()
##            sort1(myList)
##            endTime = time.time()
##            elapsedLinearTime = endTime - startTime
##            avgTime1 += elapsedLinearTime
##
##            startTime = time.time()
##            sort2(myList1)
##            endTime = time.time()
##            elapsedLinearTime = endTime - startTime
##            avgTime2 += elapsedLinearTime
##
##            startTime = time.time()
##            sort3(myList2)
##            endTime = time.time()
##            elapsedLinearTime = endTime - startTime
##            avgTime3 += elapsedLinearTime
##
##            startTime = time.time()
##            sort4(myList3)
##            endTime = time.time()
##            elapsedLinearTime = endTime - startTime
##            avgTime4 += elapsedLinearTime
##
##            startTime = time.time()
##            sort5(myList4)
##            endTime = time.time()
##            elapsedLinearTime = endTime - startTime
##            avgTime5 += elapsedLinearTime
##
##            startTime = time.time()
##            sort6(myList5)
##            endTime = time.time()
##            elapsedLinearTime = endTime - startTime
##            avgTime6 += elapsedLinearTime
##
##        avgTime1 = avgTime1/100
##        avgTime2 = avgTime2/100
##        avgTime3 = avgTime3/100
##        avgTime4 = avgTime4/100
##        avgTime5 = avgTime5/100
##        avgTime6 = avgTime6/100
##
##        print('n =\t'+ str(n) +'\tRunningTime =\t'+str(avgTime1)+'\t'+str(avgTime2))
##
##        print('n =\t'+ str(n) +'\tRunningTime =\t'+str(avgTime3)+'\t'+str(avgTime4))
##
##        print('n =\t'+ str(n) +'\tRunningTime =\t'+str(avgTime5)+'\t'+str(avgTime6))
##
##test()


    
