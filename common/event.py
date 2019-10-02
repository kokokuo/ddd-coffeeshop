import abc
import uuid
from datetime import datetime
from typing import Optional


class DomainEvent(abc.ABC):
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
        if not isinstance(other, self.__class__):
            return False
        if self.event_id == other.event_id and self.occur_date == self.occur_date:
            return True
        return False
