#!/usr/bin/env python3
import sys
import time
from trabalho_final.logger import Logger, TagTypes
import argparse
from trabalho_final.caches.static_cache import StaticCache
from trabalho_final.caches.random_cache import RandomCache
from trabalho_final.caches.lru_cache import LRUCache
from trabalho_final.caches.fifo_cache import FIFOCache
from trabalho_final.events.start_request import StartRequest
from trabalho_final.config import Config
from trabalho_final.timeline import Timeline
import traceback
from trabalho_final.stats import *

cache_map = {
    "fifo": FIFOCache,
    "lru": LRUCache,
    "random": RandomCache,
    "static": StaticCache
}

def getCaches(config):
    return [cache_map[cache[0]](cache[1], config) for cache in config.caches]


def user(config, nRequests = 10):
    
    timeline = Timeline(config)
    timeline.insert(StartRequest(config, max_requests=nRequests, cache_list=getCaches(config)))
    
    while len(timeline.timelist) > 0:
        event = timeline.advanceTime()
        config.logger.info(f'Consuming Type: {event.__class__.__name__}; RequestId: {event.request_data.request_id}, Timestamp: {event.timestamp}')
        event.handle_event(timeline)
    
    return [start_event.request_data for start_event in timeline.requests_list]





def argParser():
    ap = argparse.ArgumentParser()
    ap.add_argument('-d', '--debug',type=lambda tag: TagTypes[tag], default=TagTypes.SUCCESS , choices=list(TagTypes) ,required=False, help="debug level")
    ap.add_argument('-c', '--config', default='default_config.json', required=False, help="config file")
    ap.add_argument('-r', '--requests', type=int, default=10, required=False, help="number of requests")
    return vars(ap.parse_args())

mean

if __name__ == '__main__':
    args = argParser()
    logger = Logger(args['debug'])
    config = Config(args['config'], logger=logger)
    try:
        timeinit = time.time()
        user(config=config, nRequests=args['requests'])
        timeend = time.time()
        logger.success(f'Requests executed with success in {timeend-timeinit} seconds')
    except Exception as e:
        logger.error(f'A error occurred:\n\t {e}')
        traceback.print_exc()