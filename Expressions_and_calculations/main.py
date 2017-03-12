from tkinter import *
from expressionfactory import *
from expression import *

class CalculatorCallbackHandler:
    """A simple class that represents a parameterized button callback function. In this case, the callback adds a given string to a given TKinter StringVar object."""
    def __init__(self, stringToAdd, stringVar):
        """Takes two parameters. stringToAdd is a string. stringVar is a TKinter StringVar object to which the callback function will append stringToAdd."""
        self.__stringToAdd = stringToAdd
        self.__stringVar = stringVar

    def callback(self):
        """Adds the string to the StringVar (both given as parameters to the constructor)"""
        self.__stringVar.set(self.__stringVar.get() + self.__stringToAdd)

class CalculatorGUI:
    """A class encapsulating a TKinter calculator GUI."""
    def __init__(self, guiRoot):
        """Takes a single parameter: the TKinter root object. Constructs the window, and adds several buttons/labels."""
        #__factory is an ExpressionFactory, used to create Expression
        #objects for evaluation and translation into various formats
        self.__factory = ExpressionFactory()

        #Setting up the window
        self.__frame = Frame(guiRoot)
        #We will use grid layout
        self.__frame.grid()

        #Setting up the input "screen"
        self.__inputText = StringVar()
        self.__inputField = Label(self.__frame, textvariable = self.__inputText, borderwidth = 2, relief = SUNKEN, width = 32, justify = RIGHT, anchor = E)
        self.__inputField.grid(row = 0, column = 0, columnspan = 4)

        #Setting up the results display
        self.__outputLabels = []
        self.__outputFields = []
        self.__outputText = []
        outputStrings = ["Infix: ", "Prefix: ", "Postfix: ", "Result: "]
        for r in range(6, 10):
            self.__outputLabels.append(Label(self.__frame, text = outputStrings[r - 6], width = 8, justify = RIGHT, anchor = E))
            self.__outputLabels[r - 6].grid(row = r, column = 0)
            self.__outputText.append(StringVar())
            self.__outputFields.append(Label(self.__frame, textvariable = self.__outputText[-1], width = 24, justify = RIGHT, anchor = W))
            self.__outputFields[r - 6].grid(row = r, column = 1, columnspan = 3)

        #Setting up the buttons
        buttonLayout = [["1", "2", "3", " + "], ["4", "5", "6", " - "], ["7", "8", "9", " * "], [" ( ", "0", " ) ", " / "], ["=", "C", "-/+", " ^ "]]

        self.__buttons = []
        self.__callbackHandlers = []

        #The first 4 rows are all straightforward
        for r in range(len(buttonLayout) - 1):
            self.__buttons.append([])
            self.__callbackHandlers.append([])
            for c in range(len(buttonLayout[r])):
                self.__callbackHandlers[r].append(CalculatorCallbackHandler(buttonLayout[r][c], self.__inputText))
                self.__buttons[r].append(Button(self.__frame, text = buttonLayout[r][c], command = self.__callbackHandlers[r][c].callback, width = 5))
                self.__buttons[r][c].grid(row = 1 + r, column = c)
        
        #Do the last row separately because of all the special cases
        self.__buttons.append([])
        self.__callbackHandlers.append([])
        r = len(buttonLayout) - 1
        # = 
        #This handler is not actually used (just a placeholder in the list)
        #Real callback is below.
        self.__callbackHandlers[r].append(CalculatorCallbackHandler(buttonLayout[r][0], self.__inputText))
        self.__buttons[r].append(Button(self.__frame, text = buttonLayout[r][0], command = self.__equalsCallback, width = 5))
        self.__buttons[r][0].grid(row = len(self.__buttons), column = 0)

        # C 
        #This handler is not actually used (just a placeholder in the list)
        #Real callback is below.
        self.__callbackHandlers[r].append(CalculatorCallbackHandler(buttonLayout[r][1], self.__inputText))
        self.__buttons[r].append(Button(self.__frame, text = buttonLayout[r][1], command = self.__clearCallback, width = 5))
        self.__buttons[r][1].grid(row = len(self.__buttons), column = 1)

        # +/- 
        #This handler is not actually used (just a placeholder in the list)
        #Real callback is below.
        self.__callbackHandlers[r].append(CalculatorCallbackHandler(buttonLayout[r][2], self.__inputText))
        self.__buttons[r].append(Button(self.__frame, text = buttonLayout[r][2], command = self.__negCallback))
        self.__buttons[r][2].grid(row = len(self.__buttons), column = 2)

        # ^ 
        #This is just a regular button
        self.__callbackHandlers[r].append(CalculatorCallbackHandler(buttonLayout[r][3], self.__inputText))
        self.__buttons[r].append(Button(self.__frame, text = buttonLayout[r][3], command = self.__callbackHandlers[r][3].callback, width = 5))
        self.__buttons[r][3].grid(row = len(self.__buttons), column = 3)
        
    def __equalsCallback(self):
        """The callback function for the equals button. Gives the expression held by the StringVar __outputText to __factory to create an Expression. The expression is evaluated and translated into infix, postfix, and prefix notation. The results are displaying in the appropriate labels."""
        #Use the ExpressionFactory to create an Expression
        expr = self.__factory.createExpression(self.__inputText.get())
        #Get and display various string representations of the Expression
        self.__outputText[0].set(expr.getInfix())
        self.__outputText[1].set(expr.getPrefix())
        self.__outputText[2].set(expr.getPostfix())
        #Evaluate the Expression and display the result
        self.__outputText[3].set(expr.evaluate())

    def __clearCallback(self):
        """The callback function for the "clear" button. Clears the input text."""
        self.__inputText.set("")

    def __negCallback(self):
        """The callback function for the negate button. Determines whether the last token in the input string is a number. If it is, either adds or removes a - sign (if it is absent or present, respectively)."""
        tokenList = self.__inputText.get().split()
        #If last token is not an operator, it must be a number
        if tokenList[-1] not in "()*+-/^":
            #If the first character is a -, remove the - sign
            if tokenList[-1][0] == "-":
                tokenList[-1] = tokenList[-1][1:]
            #Otherwise, add a - sign
            else:
                tokenList[-1] = "-" + tokenList[-1]
            #Reconstruct the input text
            self.__inputText.set(' '.join(tokenList))   

def main():
    """The main function simply sets up the GUI and kicks off the TKinter loop."""
    root = Tk()
    gui = CalculatorGUI(root)
    root.mainloop()

main()
