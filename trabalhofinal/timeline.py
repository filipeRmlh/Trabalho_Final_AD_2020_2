from trabalhofinal.events.timeout import Timeout


class Timeline:
    def __init__(self):
        self.timelist = []

    def advanceTime(self):
        event = self.timelist[0]
        del self.timelist[0]
        return event

    def sort(self):
        self.timelist.sort(key = lambda e: e.timestamp)

    def insert(self, event):
        self.timelist.append(event)
        self.sort()

    def removeTimeouts(self, content):
        self.timelist = list(filter(lambda c: c is Timeout and c.content is not content , self.timelist))

    def removeRequest(self, requestId):
        self.timelist = list(filter(lambda c: c.request.Id is not requestId , self.timelist))
    
    def removeRequestContent(self, content):
        self.timelist = list(filter(lambda c: c.request.content is not content, self.timelist))