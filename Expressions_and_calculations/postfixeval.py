import sys
from stack import *

def evaluatePostfix(postfixExpr):
    tokens = postfixExpr.split()
    operandStack = Stack()

    operators = "+*/-^"

    for token in tokens:
        if token in operators:
            o1 = operandStack.pop()
            o2 = operandStack.pop()
            result = applyOperator(token, o2, o1)
            operandStack.push(result)
        else: #token is an operand, assumed to be an int
            operandStack.push(int(token))
    return operandStack.pop()

def applyOperator(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1/operand2
    elif operator == "^":
        return operand1**operand2

