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