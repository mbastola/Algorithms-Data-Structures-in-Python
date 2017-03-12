#Manil Bastola


from expression import *
from stack import *

class ExpressionFactory:
    def createExpression(self,infixStr):
        prec = {}
        prec["^"] = 4
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
         
        opStack = Stack()
        exprStack = Stack()
        tokenList = infixStr.split()
        for token in tokenList:
            if token == '(':
                opStack.push(token)
            elif token == ')':
                operator = opStack.pop()
                while operator != '(':
                    a1 = exprStack.pop()
                    a2 = exprStack.pop()
                    result = BinaryExpression(operator, a2, a1)
                    exprStack.push(result)
                    operator = opStack.pop()
                    
            elif token in prec:
                while opStack.isEmpty()==False and prec[opStack.peek()] >= prec[token]:
                     o1 = exprStack.pop()
                     o2 = exprStack.pop()
                     result = BinaryExpression(opStack.pop(), o2, o1)
                     exprStack.push(result)
                opStack.push(token)
            else:
                result = ConstantExpression(int(token))
                exprStack.push(result)
        while not opStack.isEmpty():
            a1 = opStack.pop()
            a2 = exprStack.pop()
            a3 = exprStack.pop()
            result = BinaryExpression(a1, a3, a2)
            exprStack.push(result)
        return exprStack.pop()



         
         
         
        
        
