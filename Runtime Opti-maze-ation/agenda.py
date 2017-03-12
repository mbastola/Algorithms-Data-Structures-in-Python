import abc

class Agenda(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addItem(self, item):
        return

    @abc.abstractmethod
    def getItem(self):
        return

    @abc.abstractmethod
    def isEmpty(self):
        return

    @abc.abstractmethod
    def clear(self):
        return

class StackAgenda(Agenda):
    def __init__(self):
        self.__data = []

    def addItem(self, item):
        self.__data.append(item)

    def getItem(self):
        return self.__data.pop()

    def isEmpty(self):
        return len(self.__data) == 0

    def clear(self):
        self.__data = []

class QueueAgenda(Agenda):
    def __init__(self):
        self.__data = []

    def addItem(self, item):
        self.__data.insert(0, item)

    def getItem(self):
        return self.__data.pop()

    def isEmpty(self):
        return len(self.__data) == 0

    def clear(self):
        self.__data = []
