#!/usr/bin/env python3

from statistics import mean
import multiprocessing
from multiprocessing import Process
import sys
import time
import argparse
import traceback
import numpy as np
from trabalho_final.logger import Logger, TagTypes
from trabalho_final.caches.static_cache import StaticCache
from trabalho_final.caches.random_cache import RandomCache
from trabalho_final.caches.lru_cache import LRUCache
from trabalho_final.caches.fifo_cache import FIFOCache
from trabalho_final.events.start_request import StartRequest
from trabalho_final.config import Config
from trabalho_final.timeline import Timeline
from trabalho_final.request_data import RequestData
from trabalho_final.stats import *



cache_map = {
    "fifo": FIFOCache,
    "lru": LRUCache,
    "random": RandomCache,
    "static": StaticCache
}

def generateCacheContent(N=3, size=2):
  return np.random.choice(np.arange(1, N+1),size,replace=False).tolist()

def getCaches(config):
    return [cache_map[cache[0]](cache[1], config, values=generateCacheContent(config.contentSize, cache[1])) for cache in config.caches]


def user(config, nRequests = 10):
    timeline = Timeline(config)
    StartRequest.request_id = 0
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
    ap.add_argument('-r', '--requests', type=int, default=10, required=True, help="number of requests")
    ap.add_argument('-m', '--means', type=int, default=10, required=True, help="number of means")
    return vars(ap.parse_args())


def getMeans(means, config, nRequests=10, nMeans=4000,  nGroups=1):
    iterations = int(nMeans/nGroups) if int(nMeans/nGroups) > 0 else 1
    
    for _ in range(iterations):
        requests_data = user(config, nRequests)
        requests_colleted_data = RequestData.getDataFunction(config.dataTypes, requests_data)
        mean = np.mean(requests_colleted_data)
        means.append(mean)


def parallelMeans(config, nRequests=10, nMeans=4000, nGroups=multiprocessing.cpu_count()):
    processList = []
    manager =  multiprocessing.Manager()
    means = manager.list()
    for _ in range(nGroups-1):
        process = Process(target=getMeans, args=(means, config, nRequests, nMeans, nGroups,))
        process.start()
        processList.append(process)
        
    for process in processList:
        process.join()
    return means



def main():
    args = argParser()
    logger = Logger(args['debug'])
    config = Config(args['config'], logger=logger)
    try:
        timeinit = time.time()
       
        results = parallelMeans(config=config, nRequests=args['requests'], nMeans=args['means'])
        
        printStats(getStats(results))

        plotSamples(results)
        timeend = time.time()
        logger.success(f'Requests executed with success in {timeend-timeinit} seconds')
    except Exception as e:
        logger.error(f'A error occurred:\n\t {e}')
        traceback.print_exc()


if __name__ == '__main__':
    main()