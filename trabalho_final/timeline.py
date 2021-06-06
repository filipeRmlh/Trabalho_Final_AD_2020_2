from .events.start_request import StartRequest
from .events.timeout import Timeout



class Timeline:
    def __init__(self, config):
        self.timelist = []
        self.requests_list = []
        self.config = config


    def advanceTime(self):
        event = self.timelist[0]
        if isinstance(event, StartRequest):
            self.config.logger.info(f'Request with id "{event.request_data.request_id}" saved: ')
            self.requests_list.append(event)
        del self.timelist[0]
        return event


    def sort(self):
        self.timelist.sort(key = lambda e: e.timestamp)


    def insert(self, event):
        self.timelist.append(event)
        self.sort()


    def remove_timeouts(self, current_event):
        index=0
        while index < len(self.timelist):
            evt = self.timelist[index]
            if isinstance(evt, Timeout) and evt.request_data.content is current_event.request_data.content:
                evt.request_data.end_timestamp = current_event.timestamp
                del self.timelist[index]
            index += 1


    def remove_request(self, current_event):
        self.timelist = list(filter(lambda evt: evt.request_data.Id is not current_event.request_data.Id , self.timelist))
    
    
    def remove_content(self, current_event):
        self.timelist = list(filter(lambda evt: evt.request_data.content is not current_event.request_data.content, self.timelist))
