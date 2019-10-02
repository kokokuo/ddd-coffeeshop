from typing import cast
from common.valueobj import ValueObject
from decimal import Decimal


class OrderItem(ValueObject):
    def __init__(self, product_id: str, quantity: str, price: Decimal) -> None:
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
    def price(self):
        return self._price

    def __eq__(self, other: object):
        if type(self) != type(other):
            return False
        other = cast(OrderItem, other)
        return (self.product_id, self.quantity, self.price) == (other.product_id, other.quantity, other.price)

    def __hash__(self):
        return hash((self.product_id, self.quantity, self.price))

    def __repr__(self):
        return "<OrderItem: product_id:%s, quantity=%s, price=%r>" % (self.product_id, self.quantity, self.price)
