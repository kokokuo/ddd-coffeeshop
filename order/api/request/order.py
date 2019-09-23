from marshmallow import Schema, fields


class OrderItemValidator(Schema):
    # "data_key" new naming of load_from and dump_to
    product_id = fields.Str(data_key='product_id', required=True)
    quantity = fields.Int(data_key='quantity', required=True)
    price = fields.Decimal(data_key="price", required=True)

    class Meta:
        strict = True


class CreateOrderReqValidator(Schema):
    table_no = fields.Str(data_key="table_no", required=True)
    # "many" parameter could achieve nested of list
    items = fields.Nested(OrderItemValidator, many=True)

    class Meta:
        strict = True
