from .event import Event
from .timeout import Timeout
from numpy import random

class Cache2Client(Event):
    def __init__(self, dataflow, timestamp, config):
        super().__init__(dataflow.request_id, dataflow.content, timestamp, config)

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.client2CacheRate)

    def handle_event(self, timeline):
        if self.testLoss():
            return
        timeout = Timeout(self.request_id, self.content, self.timestamp, self.config)
        timeline.insert(timeout)