from .event import Event
from numpy import random
from .timeout import Timeout
from .data_flow import DataFlow
from .client_2_cache import Client2Cache


class StartRequest(Event):
    request_id = 1

    def __init__(self, timestamp, cache_list, config):
        content = random.randint(config.contentSize)
        super().__init__(StartRequest.request_id, content, timestamp, config)
        self.cache_list = cache_list
        StartRequest.request_id += 1

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.userRequestRate)

    def handle_event(self, timeline):
        timeout = Timeout(self.request_id, self.content,
                          self.timestamp, self.config)
        timeline.insert(timeout)

        for cache in self.cache_list:
            data_flow = DataFlow(self.request_id, self.content, cache)
            cache_request = Client2Cache(
                data_flow, self.timestamp, self.config)
            timeline.insert(cache_request)

        next_request = StartRequest(
            self.timestamp, self.cache_list, self.config)
        timeline.insert(next_request)
