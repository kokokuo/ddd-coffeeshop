import abc


class IFactory(object):

    @abc.abstractmethod
    def create(self):
        raise ImportError()