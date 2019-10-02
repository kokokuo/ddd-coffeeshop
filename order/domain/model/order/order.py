from .id import OrderId
from common.aggregate import AggregateRoot


class Order(AggregateRoot):
    def __init__(self, id: OrderId, table_no: str, items) -> None:
        pass
