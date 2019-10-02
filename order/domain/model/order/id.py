from datetime import datetime
from common.identity import EntityId


class OrderId(EntityId):
    def __init__(self, serial_no: int, occur_date: datetime) -> None:
        super(OrderId, self).__init__("ORD", serial_no, occur_date)
