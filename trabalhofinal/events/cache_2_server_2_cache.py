from .event import Event
class Cache2Server2Cache(Event):
    def __init__(self, request_data, timestamp, config, cache=None):
        super().__init__(request_data, timestamp, config, cache)
    
    def new_timestamp(self, timestamp, config):
        return super().new_timestamp(timestamp, config)

    def handle_event(self, timeline):
        return super().handle_event(timeline)