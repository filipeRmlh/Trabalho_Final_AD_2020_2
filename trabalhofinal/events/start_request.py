from trabalhofinal import request_data
from .event import Event
from numpy import random
from .timeout import Timeout
from trabalhofinal.request_data import RequestData
from .client_2_cache import Client2Cache
from trabalhofinal.config import Config


class StartRequest(Event):
    request_id = 0

    def __init__(self, timestamp=0, config=Config(), cacheList=[]):
        request_data = RequestData(
            request_id=StartRequest.request_id,
            content=random.randint(config.contentSize)
        )
        super().__init__(request_data, timestamp, config)
        self.cacheList = cacheList
        StartRequest.request_id += 1

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.userRequestRate)

    def handle_event(self, timeline, max_requests=100000):
        timeout = Timeout(self.request_id, self.content,
                          self.timestamp, self.config)
        timeline.insert(timeout)

        for cache in self.cache_list:
            cache_request = Client2Cache(
                self.request_data, self.timestamp, self.config, cache)
            timeline.insert(cache_request)

        if self.request_data.request_id < max_requests:
            next_request = StartRequest(
                self.timestamp, self.config, self.cache_list
            )
            timeline.insert(next_request)
