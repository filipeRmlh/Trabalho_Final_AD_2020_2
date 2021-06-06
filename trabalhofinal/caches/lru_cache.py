from .cache import Cache

class LRUCache(Cache):
  def __init__(self, capacity, values = None):
        super().__init__(capacity, values)

  def check_value(self, value):
    for element in self.content:
      if value == element:
        self.content = list(filter(lambda c: c is not element ,self.content)) #send element to last position
        self.content.append(element)
        return True
    return False

  def send_value(self, value):
    contains_value = False
    for element in self.content:
      if value == element:
        contains_value = True
    
    if not contains_value:
      self.content.append(value)

    if len(self.content) > self.capacity:
      self.content.pop(0)