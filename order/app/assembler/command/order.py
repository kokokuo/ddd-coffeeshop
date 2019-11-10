from order.app.dto.command.order import CreateOrderCommand, CreateOrderItemCommand


class CreateOrderAssembler(object):

    @classmethod
    def from_request(cls, reqargs: dict) -> CreateOrderCommand:
        item_args = reqargs["items"]
        reqargs["items"] = [CreateOrderItemCommand(**item) for item in item_args]
        return CreateOrderCommand(**reqargs)
