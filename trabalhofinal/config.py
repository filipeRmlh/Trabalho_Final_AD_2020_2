class Config:
    def __init__(
        self,
        client2CacheRate,
        client2CacheP,
        timeoutRate,
        cache2Server2Cache,
        alternativeServerRate,
        userRequestRate,
        contentSize = 3,
        cacheSizes = [2, 2]
    ):
        #mi
        self.client2CacheRate = client2CacheRate
        #P
        self.client2CacheP = client2CacheP
        #alpha
        self.timeoutRate = timeoutRate
        #theta
        self.cache2Server2Cache = cache2Server2Cache
        #gamma
        self.alternativeServerRate = alternativeServerRate
        #lambda
        self.userRequestRate = userRequestRate
        #N
        self.contentSize = contentSize
        #M
        self.cacheSizes = cacheSizes
