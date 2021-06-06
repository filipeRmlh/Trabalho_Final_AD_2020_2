import numpy as np
from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, request_id, content, timestamp, config):
        self.request_id = request_id
        self.content = content
        self.
        self.timestamp = self.new_timestamp(timestamp, config)
        self.config = config
    
    @abstractmethod
    def new_timestamp(self, timestamp, config):
        pass

    @abstractmethod
    def handle_event(self, timeline):
        pass

    def exp_delay(rate):
        return np.random.exponential(1/rate)