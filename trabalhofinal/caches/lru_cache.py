from .cache import Cache

class LRUCache(Cache):
  def __init__(self, capacity, values = None):
        super().__init__(capacity, values)

  def checkValue(self, value):
    for element in self.content:
      if value == element:
        self.content = list(filter(lambda c: c is not element ,self.content)) #send element to last position
        self.content.append(element)
        return True
    return False

  def SendValue(self, value):
    containsValue = False
    for element in self.content:
      if value == element:
        containsValue = True
    
    if not containsValue:
      self.content.append(value)

    if len(self.content) > self.capacity:
      self.content.pop(0)