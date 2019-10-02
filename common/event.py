import abc
import uuid
from datetime import datetime
from typing import Optional, cast, TypeVar


class DomainEvent(abc.ABC):
    @abc.abstractmethod
    def __init__(self, occur_date: Optional[datetime] = None):
        self._event_id = uuid.uuid1()
        self._occur_date = occur_date if occur_date else datetime.utcnow()

    @property
    def event_id(self) -> uuid.UUID:
        return self._event_id

    @property
    def occur_date(self) -> datetime:
        return self._occur_date

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return False
        other = cast(DomainEvent, other)
        return (self.event_id, self.occur_date) == (other.event_id, other.occur_date)
