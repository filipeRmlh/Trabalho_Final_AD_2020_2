from .event import Event
from .request_backup import RequestBackup
class Timeout(Event):
    def __init__(self, request_id, content, timestamp, config):
        super().__init__(request_id, content, timestamp, config)

    def new_timestamp(self, timestamp, config):
        return timestamp + self.exp_delay(config.timeoutRate)

    def handle_event(self, timeline):
        request_backup = RequestBackup(self.request_id, self.content, self.timestamp, self.config)
        timeline.insert(request_backup)
