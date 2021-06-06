from abc import abstractmethod

class Cache():
    def __init__(self, capacity, values):
        self.capacity = capacity

        if values is not None and capacity is not len(values):
          raise Exception("Cache initialization array should have number of elements equal to cache capacity")

        if values != None:
          self.content = values
        else:
          self.content = []

    @abstractmethod
    def checkValue(self, value):
        pass

    @abstractmethod
    def sendValue(self,value):
        pass