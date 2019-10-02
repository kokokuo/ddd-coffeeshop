import abc
from .identity import EntityId


class Entity(abc.ABC):
    def __init__(self, id: EntityId):
        self._id = id

    @property
    def id(self) -> EntityId:
        return self._id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        if self._id == other.id:
            return True
        return False

    def __str__(self):
        return str(self._id)
