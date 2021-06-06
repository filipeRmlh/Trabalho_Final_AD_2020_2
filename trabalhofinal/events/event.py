import numpy as np
from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, request_data, timestamp, config, cache = None):
        self.timestamp = self.new_timestamp(timestamp, config)
        self.request_data = request_data
        self.cache = cache
        self.config = config
    
    @abstractmethod
    def new_timestamp(self, timestamp, config):
        pass

    @abstractmethod
    def handle_event(self, timeline):
        pass

    def exp_delay(rate):
        return np.random.exponential(1/rate)