from typing import List, TypeVar, Optional, cast
from datetime import datetime
from decimal import Decimal
from .id import OrderId
from .item import OrderItem
from .status import OrderStatus
from common.aggregate import AggregateRoot, Entity


class Order(AggregateRoot):
    def __init__(self,
                 order_id: OrderId,
                 table_no: str,
                 items: List[OrderItem],
                 status: OrderStatus,
                 createtd_at: datetime,
                 modified_at: Optional[datetime] = None) -> None:
        super(Order, self).__init__(order_id)
        self._table_no = table_no
        self._items = items
        self._status = status
        self._createtd_at = createtd_at
        self._modified_at = modified_at

    @classmethod
    def create(cls, order_id: OrderId, table_no: str, items: List[OrderItem]) -> "Order":
        return cls(order_id, table_no, items, OrderStatus.INITIAL, datetime.utcnow())

    @property
    def id(self) -> OrderId:
        return self.id

    @property
    def table_no(self) -> str:
        return self._table_no

    @property
    def items(self) -> List[OrderItem]:
        return self._items

    @property
    def status(self) -> OrderStatus:
        return self._status

    @property
    def total_fee(self) -> Decimal:
        item: OrderItem
        total = sum((item.price for item in self.items))
        return cast(Decimal, total)

    @property
    def createtd_at(self) -> datetime:
        return self._createtd_at

    @property
    def modified_at(self) -> Optional[datetime]:
        return self._modified_at

    def __repr__(self) -> str:
        return "<Order: id:{}, \n\
                table_no={}, \n\
                tems={}, \n\
                status={}, \n\
                total_fee={}, \n\
                createtd_at={}, \n\
                modified_at={}>" \
            .format(self.id,
                    self.table_no,
                    self.items,
                    self.status,
                    self.total_fee,
                    self.createtd_at,
                    self.modified_at)
