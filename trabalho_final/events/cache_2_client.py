from .event import Event

class Cache2Client(Event):
    def __init__(self, request_data, timestamp, config, cache = None):
        super().__init__(request_data, timestamp, config, cache)


    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.client2CacheRate)


    def handle_event(self, timeline):
        if(self.request_data.timeout is not None):
            return
        
        self.request_data.timeout = False
        self.request_data.end_timestamp = self.timestamp

        timeline.remove_timeouts(self)