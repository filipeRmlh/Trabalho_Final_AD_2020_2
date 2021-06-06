from .cache import Cache



class FIFOCache(Cache):
    def __init__(self, capacity, config, values = None):
        super().__init__(capacity, config, values)


    def check_value(self, value):
      return True if value in self.content else False
      

    def send_value(self, value):
      self.content.append(value)

      if len(self.content) > self.capacity:
        self.content.pop(0)