from typing import List
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class CreatedOrderItemResult(object):
    product_id: str
    quantity: int
    price: Decimal
    fee: Decimal


@dataclass(frozen=True)
class CreatedOrderResult(object):
    id: str
    status: str
    items: List[CreatedOrderItemResult]
    total_fee: Decimal
    created_date: datetime
    modified_date: datetime
