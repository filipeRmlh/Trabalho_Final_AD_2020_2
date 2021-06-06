from trabalho_final.events.cache_2_client import Cache2Client
from .event import Event



class Cache2Server2Cache(Event):
    def __init__(self, request_data, timestamp, config, cache = None):
        super().__init__(request_data, timestamp, config, cache)
    

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.cache2Server2CacheRate)


    def handle_event(self, timeline):
        self.cache.send_value(self.request_data.content)
        cache2Client = Cache2Client(self.request_data, self.timestamp, self.config, cache=self.cache)
        timeline.insert(cache2Client)