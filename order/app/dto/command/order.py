from typing import List
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CreateOrderItemCommand(object):
    product_id: str
    quantity: int
    price: Decimal


@dataclass(frozen=True)
class CreateOrderCommand(object):
    table_no: str
    items: List[CreateOrderItemCommand]
