class RequestData:
    def __init__(
        self,
        request_id=None,
        content=None,
        init_timestamp = 0,
        end_timestamp = None
    ):
        self.request_id = request_id
        self.content = content
        self.init_timestamp = init_timestamp
        self.end_timestamp = end_timestamp