from .event import Event
from .request_backup import RequestBackup
class Timeout(Event):
    def __init__(self, request_data, timestamp, config):
        super().__init__(request_data, timestamp, config)

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.timeoutRate)

    def handle_event(self, timeline):
        request_backup = RequestBackup(self.request_data, self.timestamp, self.config)
        timeline.insert(request_backup)
