from .cache import Cache
from numpy import random

class RandomCache(Cache):
  def __init__(self, capacity, values = None):
        super().__init__(capacity, values)

  def check_value(self, value):
    for element in self.content:
      if value == element:
        return True
    return False

  def send_value(self, value):
    if not self.check_value(value):
      if len(self.content) == self.capacity:
        random_index = random.randint(0, self.capacity)
        self.content = self.content.pop(random_index)

    self.content.append(value)