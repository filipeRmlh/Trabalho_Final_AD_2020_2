from abc import abstractmethod



class Cache():
    def __init__(self, capacity, config, values):
        self.capacity = capacity

        if values is not None and capacity is not len(values):
          raise Exception("Cache initialization array should have number of elements equal to cache capacity")

        if values != None:
          self.content = values
        else:
          self.content = []


    @abstractmethod
    def check_value(self, value):
        pass


    @abstractmethod
    def send_value(self,value):
        pass