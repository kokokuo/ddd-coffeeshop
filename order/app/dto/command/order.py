from typing import List
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OrderItem(object):
    product_id: str
    quantity: int
    price: Decimal


@dataclass
class CreateOrderCommand(object):
    table_no: str
    items: List[OrderItem]
