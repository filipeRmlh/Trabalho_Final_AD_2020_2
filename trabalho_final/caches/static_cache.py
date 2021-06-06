from .cache import Cache



class StaticCache(Cache):
  def __init__(self, capacity, config, values = None):
        super().__init__(capacity, config, values)


  def check_value(self, value):
    return True if value in self.content else False


  def send_value(self, value):
    if len(self.content) < self.capacity and (not self.check_value(value)):
      self.content.append(value)