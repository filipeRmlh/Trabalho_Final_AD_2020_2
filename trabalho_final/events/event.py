import numpy as np
from abc import ABC, abstractmethod



class Event(ABC):
    def __init__(self, request_data, timestamp, config, cache = None):
        self.request_data = request_data
        self.cache = cache
        self.config = config
        self.timestamp = self.new_timestamp(timestamp, config)
        #print("Creating Type: ",self.__class__.__name__, "Request: ", self.request_data.request_id, "Timestamp: " ,self.timestamp)
    

    @abstractmethod
    def new_timestamp(self, timestamp, config):
        pass


    @abstractmethod
    def handle_event(self, timeline):
        pass
    

    def exp_delay(self, rate):
        return np.inf if rate == 0 else np.random.exponential(1/rate)