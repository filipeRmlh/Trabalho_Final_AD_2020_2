from .cache_2_server_2_cache import Cache2Server2Cache
from .cache_2_client import Cache2Client
from .event import Event
from numpy import random



class Client2Cache(Event):
    def __init__(self, request_data, timestamp, config, cache = None):
        super().__init__(request_data, timestamp, config, cache)


    def test_loss(self):
        return random.random() > self.config.client2CacheP


    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.client2CacheRate)


    def handle_event(self, timeline):
        if self.test_loss():
            return

        if self.cache.check_value(self.request_data.content):
            self.request_data.cache_hit = True
            cache2client = Cache2Client(self.request_data,self.timestamp, self.config, self.cache)
            timeline.insert(cache2client)
        else:
            cache2Server2Cache = Cache2Server2Cache(self.request_data, self.timestamp, self.config, cache=self.cache)
            timeline.insert(cache2Server2Cache)