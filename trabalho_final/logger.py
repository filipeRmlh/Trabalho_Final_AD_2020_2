from enum import Enum
from termcolor import colored as color

    
class TagTypes(Enum):
    NO_DEBUG=0
    ERROR=1
    WARN=2
    INFO=3
    DEBUG=4
    SUCCESS=5

class Logger:
    def __init__(self, debugLevel=TagTypes.NO_DEBUG):
        self.debugLevel = debugLevel

    def mapColorTag(self, enum):
        mapTag = {
            "ERROR":'red',
            "WARN":'yellow',
            "SUCCESS":'green',
            "INFO":'cyan',
            "DEBUG":'magenta'
        }
        return mapTag[enum.name]

    def error(self, msg):
        self.msg(msg, TagTypes.ERROR)

    def warn(self, msg):
        self.msg(msg, TagTypes.WARN)

    def success(self, msg):
        self.msg(msg, TagTypes.SUCCESS)

    def info(self, msg):
        self.msg(msg, TagTypes.INFO)

    def msg(self, msg, TAG=TagTypes.DEBUG):
        if TAG.value >= self.debugLevel.value:
            tagColor = self.mapColorTag(TAG)
            print(color("["+TAG.name+"]: ", tagColor) + msg)

logger = Logger()