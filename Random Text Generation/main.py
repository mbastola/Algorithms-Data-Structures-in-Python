from textgenerator import *
import sys

def main(myfile, numWords, order):
    myGen = OrderKTextGenerator(int(order))
    myFin = open(myfile,'r')
    text = ''
    for line in myFin:
        text += line
    myGen.train(text)
    myFin.close()
    print(myGen.generateText(int(numWords)))

main(sys.argv[1],sys.argv[2],sys.argv[3])
