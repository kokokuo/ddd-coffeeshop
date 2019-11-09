from order.domain.model.order import Order, OrderItem
from order.app.dto.results.order import CreatedOrderResult, CreatedOrderItemResult


class CreatedOrderAssembler(object):
    @classmethod
    def to_result(cls, order: Order) -> CreatedOrderResult:
        item: OrderItem
        items = [
            CreatedOrderItemResult(
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price,
                fee=item.fee
            ) for item in order.items
        ]

        return CreatedOrderResult(
            id=order.id,
            status=order.status.value,
            items=items,
            total_fee=order.total_fee,
            takeout=order.takeout,
            created_date=order.createtd_at,
            modified_date=order.modified_at)
