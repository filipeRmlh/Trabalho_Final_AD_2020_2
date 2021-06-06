from .cache import Cache

class StaticCache(Cache):
  def __init__(self, capacity, values = None):
        super().__init__(capacity,values)

  def check_value(self, value):
    for element in self.content:
      if value == element:
        return True
    return False

  def send_value(self, value):
    if len(self.content) < self.capacity and (not self.check_value(value)):
      self.content.append(value)