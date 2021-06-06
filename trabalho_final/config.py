from trabalho_final.caches import cache
from numpy import inf
import json


class Config:
    def __init__(
        self,
        file_path='default_config.json',
        client2CacheRate = None,
        client2CacheP = None,
        timeoutRate = None,
        cache2Server2CacheRate = None,
        alternativeServerRate = None,
        userRequestRate = None,
        contentSize = None,
        caches = None,
        logger = None
    ):
        config = self.parse(file_path)
        #mi
        self.client2CacheRate = self.parse_inf(config['Client2CacheRate'] if client2CacheRate is None else client2CacheRate)
        #P
        self.client2CacheP = self.parse_inf(config['Client2CacheP'] if client2CacheP is None else client2CacheP)
        #alpha
        self.timeoutRate = self.parse_inf(config['TimeoutRate'] if timeoutRate is None else timeoutRate)
        #theta
        self.cache2Server2CacheRate = self.parse_inf(config['Cache2Server2CacheRate'] if cache2Server2CacheRate is None else cache2Server2CacheRate)
        #gamma
        self.alternativeServerRate = self.parse_inf(config['AlternativeServerRate'] if alternativeServerRate is None else alternativeServerRate)
        #lambda
        self.userRequestRate = self.parse_inf(config['UserRequestRate'] if userRequestRate is None else userRequestRate)
        #N
        self.contentSize = self.parse_inf(config['ContentSize'] if contentSize is None else contentSize)
        #M
        self.caches = config['Caches'] if caches is None else caches

        self.logger = logger

    
    def parse_inf(self, content):
        return inf if content == 'inf' else content

    def parse(self, file_path='default_config.json'):
        file = open(file_path, 'r')
        config = json.load(file)
        file.close()
        return config
        

