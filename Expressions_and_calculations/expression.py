##Manil Bastola


import abc

class Expression(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def evaluate():
        return

    @abc.abstractmethod
    def getInfix():
        return

    @abc.abstractmethod
    def getPostfix():
        return
    
    @abc.abstractmethod
    def getPrefix():
        return

class ConstantExpression(Expression):
    def __init__(self, integer):
        self.integer = integer

    def evaluate(self):
        return self.integer

    def getInfix(self):
        return str(self.integer)

    def getPostfix(self):
        return str(self.integer)

    def getPrefix(self):
        return str(self.integer)

    def __str__(self):
        return str(self.integer)

class BinaryExpression(Expression):
    def __init__(self, operator, expr1, expr2):
        self.operator = operator
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if isinstance(self.expr1,ErrorExpression) or isinstance(self.expr1,ErrorExpression):
            return 0
        else:
            if self.operator == '+':
                return self.expr1.evaluate() + self.expr2.evaluate()
            elif self.operator == '-':
                return self.expr1.evaluate() - self.expr2.evaluate()
            elif self.operator == '*':
                return self.expr1.evaluate() * self.expr2.evaluate()
            elif self.operator == '/':
                return self.expr1.evaluate() / self.expr2.evaluate()
            elif self.operator == '^':
                return self.expr1.evaluate() ** self.expr2.evaluate()
        

    def getInfix(self):
        return self.expr1.getInfix() + self.operator + self.expr2.getInfix()

    def getPostfix(self):
        return self.expr1.getPostfix() + self.expr2.getPostfix() + self.operator 

    def getPrefix(self):
        return self.operator + self.expr1.getPrefix() + self.expr2.getPrefix()

    def __str__(self):
        return str(self.evaluate())

class ErrorExpression(Expression):
    def __init__(self, errorstr):
        self.errorstr = errorstr
        
    def evaluate(self):
        return 0

    def getInfix(self):
        return self.errorstr

    def getPostfix(self):
        return self.errorstr
    
    def getPrefix(self):
        return self.errorstr
    



    

        

        

    
