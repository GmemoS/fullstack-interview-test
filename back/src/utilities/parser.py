from collections import deque
from datetime import date, datetime
from decimal import Decimal
from json import JSONEncoder
from typing import Generator


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        elif isinstance(o, (set, deque, Generator)):
            return tuple(o)
        elif isinstance(o, (datetime, date)):
            return o.isoformat()

        return super().default(o)
