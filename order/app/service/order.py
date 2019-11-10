from sqlalchemy.orm import Session
from order.app.assembler.results.order import CreatedOrderAssembler
from order.app.dto.command.order import CreateOrderCommand, CreateOrderItemCommand
from order.app.dto.results.order import CreatedOrderResult
from order.domain.model.order import Order, OrderId, OrderItem
from order.domain.model.order.repository import IOrderRepository
from order.infrastructure.repository.sqlalchemy import dbo
from order.infrastructure.repository.sqlalchemy.command import order_repository


class OrderService(object):
    def __init__(self, session: Session, order_repository: IOrderRepository):
        self._session = session
        self._order_repo = order_repository

    def create_order(self, command: CreateOrderCommand) -> CreatedOrderResult:
        # import pdb; pdb.set_trace()
        try:
            order_id: OrderId = self._order_repo.generate_id()
            # TODO: 改成從 Repository 做 Product Id 的檢查，並透過一個 OrderItemFactory 建立 OrderItem
            item: CreateOrderItemCommand

            items = [
                OrderItem(
                    item.product_id,
                    item.quantity,
                    item.price
                ) for item in command.items
            ]
            order = Order.create(order_id, command.table_no, command.takeout, items)
            self._order_repo.save(order)
            self._session.commit()
            return CreatedOrderAssembler.to_result(order)
        except Exception as e:
            self._session.rollback()
            raise e


order_service = OrderService(dbo.session, order_repository)
