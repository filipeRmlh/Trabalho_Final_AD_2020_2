#!/usr/bin/env python3

from trabalhofinal.events.cache_2_client import Cache2Client
from trabalhofinal.events.start_request import StartRequest
from trabalhofinal.config import Config
from trabalhofinal.timeline import Timeline

def user(nRequests = 1000, config = Config()):
    timeline = Timeline()
    timeline.insert(StartRequest())
    i=0
    while i < nRequests:
        event = timeline.advanceTime()
        event.handle_event()
        if event is StartRequest:
            i+=1
        

if __name__ == '__main__':
    user()