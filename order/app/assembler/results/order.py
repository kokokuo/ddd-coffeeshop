from order.domain.model.order import Order, OrderItem
from order.app.dto.results.order import CreatedOrderResult, CreatedOrderItemResult


class CreatedOrderAssembler(object):
    @classmethod
    def to_result(cls, order_do: Order) -> None:
        item: OrderItem
        items = [
            CreatedOrderItemResult(
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price,
                fee=item.fee
            ) for item in order_do.items
        ]

        return CreatedOrderResult(
            id=order_do.id,
            status=order_do.status,
            items=items,
            created_date=order_do.createtd_at,
            modified_date=order_do.modified_at)
