from .cache import Cache

class StaticCache(Cache):
  def __init__(self, capacity, values = None):
        super().__init__(capacity,values)

  def checkValue(self, value):
    for element in self.content:
      if value == element:
        return True
    return False

  def sendValue(self, value):
    if len(self.content) < self.capacity and (not self.checkValue(value)):
      self.content.append(value)