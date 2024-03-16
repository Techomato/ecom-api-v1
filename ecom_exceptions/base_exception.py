from abc import ABC
from typing import Optional


class ECOMBaseException(ABC, Exception):
    def __init__(self, name: Optional[str], msg: Optional[str], status):
        if msg:
            self.msg = msg
        if name:
            self.name = name
        self.status = status
