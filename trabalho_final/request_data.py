class RequestData:
    def __init__(
        self,
        request_id=None,
        content=None,
        init_timestamp = 0,
        end_timestamp = None,
        timeout=None,
        cache_hit=False
    ):
        self.request_id = request_id
        self.content = content
        self.timeout = timeout
        self.init_timestamp = init_timestamp
        self.end_timestamp = end_timestamp
        self.cache_hit = cache_hit

    def getDataFunction(dataType, request_data):
        dataTypes = {
            "cache_hits": RequestData.getDataCacheHits,
            "delays": RequestData.getDataDelays,
            "init_timestamps": RequestData.getDataInitTimestamps,
            "end_timestamps": RequestData.getDataEndTimestamps
        }
        return dataTypes[dataType](request_data)

    def getDataCacheHits(requests_data):
        return [1 if data.cache_hit else 0  for data in requests_data]

    def getDataDelays(requests_data):
        return [(data.end_timestamp-data.init_timestamp) for data in requests_data]

    def getDataInitTimestamps(requests_data):
        return [data.init_timestamp for data in requests_data]
        
    def getDataEndTimestamps(requests_data):
        return [data.end_timestamp for data in requests_data]