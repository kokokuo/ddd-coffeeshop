import abc


class ValueObject(abc.ABC):

    @abc.abstractmethod
    def __eq__(self, other: object):
        raise NotImplementedError()

    @abc.abstractmethod
    def __hash__(self):
        raise NotImplementedError()
