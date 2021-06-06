from .cache import Cache

class FIFOCache(Cache):
    def __init__(self, capacity, values = None):
        super().__init__(capacity, values)

    def check_value(self, value):
      for element in self.content:
        if value == element:
          return True

      return False

    def send_value(self, value):
      self.content.append(value)

      if len(self.content) > self.capacity:
        self.content.pop(0)