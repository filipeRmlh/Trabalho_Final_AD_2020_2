from .event import Event



class RequestBackup(Event):
    def __init__(self, request_data, timestamp, config, cache = None):
        super().__init__(request_data, timestamp, config, cache)


    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.alternativeServerRate)


    def handle_event(self, timeline):
        if self.request_data.end_timestamp is None:
            timeline.remove_timeouts(self)
            self.request_data.end_timestamp = self.timestamp

        
