from datetime import datetime
from common.id import EntityId


class OrderId(EntityId):
    def __init__(self, serial_no: int, occur_date: datetime) -> None:
        super(OrderId, self).__init__("ORD", serial_no, occur_date)

    # TODO: 之後要拔掉，初始化是透過 Repository 建立 OrderId() 來的
    @classmethod
    def create(cls) -> "OrderId":
        return cls(0, datetime.utcnow())
