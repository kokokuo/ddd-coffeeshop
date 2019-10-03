from typing import cast
from common.valueobj import ValueObject
from datetime import datetime
from decimal import Decimal


class OrderItem(ValueObject):
    def __init__(self,
                 product_id: str,
                 quantity: str,
                 price: Decimal) -> None:

        self._product_id = product_id
        self._quantity = quantity
        self._price = price

    @property
    def product_id(self):
        return self._product_id

    @property
    def quantity(self):
        return self._quantity

    @property
    def fee(self) -> Decimal:
        return self.price * self.quantity

    @property
    def price(self):
        return self._price

    def __eq__(self, other: object):
        if type(self) != type(other):
            return False
        other = cast(OrderItem, other)
        return (self.product_id,
                self.quantity,
                self.price,
                self.fee) == (other.product_id,
                              other.quantity,
                              other.price,
                              other.fee)

    def __hash__(self) -> int:
        return hash((self.product_id, self.quantity, self.price, self.fee))

    def __repr__(self) -> str:
        return "<OrderItem: product_id:{}, \n\
                quantity={}, \n\
                price={}, \n\
                fee={}>" \
            .format(self.product_id,
                    self.quantity,
                    self.price,
                    self.fee)
