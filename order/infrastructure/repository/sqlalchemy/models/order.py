from typing import List, Dict
import json
from order.infrastructure.repository.sqlalchemy import dbo
from .common import SystemInfo


class OrderTable(SystemInfo):
    __tablename__ = "orders"

    id = dbo.Column(dbo.String, primary_key=True)
    table_no = dbo.Column(dbo.String(3), nullable=False)
    status = dbo.Column(dbo.String(32), nullable=False)
    items = dbo.Column(dbo.UnicodeText, nullable=False)
    total_fee = dbo.Colum(dbo.Numeric(12, 2), nullable=False)
    takeout = dbo.Colum(dbo.Boolean, nullable=False, default=True)

    def load_items(self) -> List[Dict[str, str]]:
        return json.loads(self.items)

    def __repr__(self):
        return "<OrderTable:\n\
        id=%s\n\
        table_no=%s\n\
        status=%s\n\
        total_fee=%r\n\
        items=%r\n\
        takeout=%r>" % (
            self.id,
            self.table_no,
            self.status,
            self.total_fee,
            self.load_items(),
            self.takeout
        )
