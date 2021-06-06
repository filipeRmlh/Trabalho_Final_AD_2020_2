from ..request_data import RequestData
from .event import Event
from numpy import random
from .timeout import Timeout
from .client_2_cache import Client2Cache
from ..config import Config



class StartRequest(Event):
    request_id = 0


    def __init__(self, config, timestamp=0, cache_list=[], max_requests = 10000):
        request_data = RequestData(
            request_id=StartRequest.request_id,
            content=random.randint(config.contentSize)
        )
        super().__init__(request_data, timestamp, config)
        self.cache_list = cache_list
        StartRequest.request_id += 1
        self.max_requests = max_requests


    def new_timestamp(self, timestamp, config):
        new_time = timestamp + self.exp_delay(config.userRequestRate)
        self.request_data.init_timestamp = new_time
        return new_time


    def handle_event(self, timeline):
        timeout = Timeout(self.request_data, 
                          self.timestamp, self.config)
        timeline.insert(timeout)

        for cache in self.cache_list:
            cache_request = Client2Cache(
                self.request_data, self.timestamp, self.config, cache)
            timeline.insert(cache_request)

        if self.request_data.request_id < self.max_requests-1:
            next_request = StartRequest(
                self.config,
                self.timestamp,
                self.cache_list,
                self.max_requests
            )
            timeline.insert(next_request)
