from marshmallow import fields
from plugin.marshmallow.shema import DumpSchema


class OrderItemResp(DumpSchema):
    product_id = fields.Str(data_key='product_id', required=True)
    quantity = fields.Int(data_key='quantity', required=True)
    price = fields.Decimal(data_key="price", as_string=True, required=True)
    fee = fields.Decimal(data_key="fee", as_string=True, required=True)

    class Meta:
        strict = True


class CreatedOrderResp(DumpSchema):
    id = fields.Str(data_key='id', required=True)
    status = fields.Str(data_key='status', required=True)
    items = fields.Nested(OrderItemResp, data_key="items", many=True, required=True)
    created_at = fields.DateTime(data_key="created_at", many=True, required=True)
    modified_at = fields.DateTime(data_key="modified_at", many=True, required=True)

    class Meta:
        strict = True
