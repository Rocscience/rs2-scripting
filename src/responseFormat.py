from enum import Enum

class functionStatus(Enum):
    success = 1
    notFound = 2
    failure = 3

class functionResponse:
    def __init__(self, status: functionStatus, value, exception=None):
        self.status = status
        self.value = value
        self.exception = exception
