from datetime import datetime
from common.id import EntityId


class OrderId(EntityId):
    def __init__(self, serial_no: int, createtd_at: datetime) -> None:
        super(OrderId, self).__init__("ORD", serial_no, createtd_at)
