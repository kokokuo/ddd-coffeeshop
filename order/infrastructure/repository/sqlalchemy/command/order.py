
import json
from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.expression import false, true, func
from order.domain.model.order import Order, OrderId, OrderStatus, OrderItem
from order.domain.model.order.repository import IOrderRepository
from order.infrastructure.repository.sqlalchemy import dbo
from order.infrastructure.repository.sqlalchemy.models import OrderTable


class OrderRepository(IOrderRepository):
    def __init__(self, session: Session) -> None:
        # Unit Of Work for SQLAlchmey
        self._session = session

    def _assemble_do(self, order_table: OrderTable) -> Order:
        items_vo = [
            OrderItem(
                item["product_id"],
                int(item["quantity"]),
                Decimal(item["price"])
            )
            for item in order_table.load_items()
        ]
        order = Order(
            OrderId(order_table.id, order_table.created_at),
            order_table.table_no,
            items_vo,
            OrderStatus(order_table.status),
            order_table.created_at,
            order_table.modified_at
        )
        return order

    def generate_id(self) -> OrderId:
        db_query: Query = self._session.query(OrderTable).filter(
            OrderTable.mark_deleted == false()
        )
        db_query.statement.with_only_columns([func.count()]).order_by(None)
        count = db_query.scalar()
        order_id = OrderId(count, datetime.utcnow())
        return order_id

    def get_by(self, order_id: OrderId) -> Order:
        query: Query = self._session.query(OrderTable).filter(
            OrderTable.id == str(order_id),
            OrderTable.mark_deleted == false()
        )
        order_table: OrderTable = query.scalar()
        # TODO: 補上 Not Found Expcetion
        order = self._assemble_do(order_table)
        return order

    def save(self, order: Order) -> Order:
        item: OrderItem
        items = [
            {
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": item.price
            } for item in order.items
        ]

        order_args = {
            "id": str(order.id),
            "table_no": order.table_no,
            "status": order.status.value,
            "items": items,
            "total_fee": order.total_fee,
            "takeout": order.takeout,
            "created_at": order.createtd_at,
            "modified_at": order.modified_at,

        }
        order_table = OrderTable(**order_args)
        self._session.add(order_table)
        self._session.flush()
        self._session.add()
        return order


order_repository = OrderRepository(dbo.session)
