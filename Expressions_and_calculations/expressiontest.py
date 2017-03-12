##Manil Bastola


from stack import *
from expression import *

def infixToPostfix(infixStr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postFixList = []
    tokenList = infixStr.split()
    for token in tokenList:      
        if token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postFixList.append(topToken)
                topToken = opStack.pop()
        elif token in prec:
            while opStack.isEmpty()==False and prec[opStack.peek()] >= prec[token]:
                postFixList.append(opStack.pop())
            opStack.push(token)
        else:
             postFixList.append(token)
    while not opStack.isEmpty():
        postFixList.append(opStack.pop())

    return ''.join(postFixList)

def postfixToExpression(postfixStr):
    tokens = postfixStr.split()
    operandStack = Stack()

    operators = "+*/-^"

    for token in tokens:
        if token in operators:
            o1 = operandStack.pop()
            o2 = operandStack.pop()
            result = BinaryExpression(token, o2, o1)
            operandStack.push(result)
        else: 
            result = ConstantExpression(int(token))
            operandStack.push(result)
    return operandStack.pop()
    



    

        



    
    




        
                
                
