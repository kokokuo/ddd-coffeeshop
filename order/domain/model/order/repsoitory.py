import abc
from order.domain.model.order import OrderId, Order


class IOrderRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, order: Order) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by(self, id: OrderId) -> Order:
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_id(self) -> OrderId:
        raise NotImplementedError()
