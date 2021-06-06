from .event import Event

class RequestBackup(Event):
    def __init__(self, dataFlow, timestamp, config):
        super().__init__(dataFlow.request_id, dataFlow.content, timestamp, config)

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.alternativeServerRate)

    def handle_event(self, timeline):
        raise NotImplementedError()
