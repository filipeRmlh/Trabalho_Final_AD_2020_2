from .event import Event
from .timeout import Timeout
from numpy import random

class Cache2Client(Event):
    def __init__(self, request_data, timestamp, config, cache = None):
        super().__init__(request_data, timestamp, config, cache)

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.client2CacheRate)

    def handle_event(self, timeline):
        timeline.remove_timeouts(self.request_data)