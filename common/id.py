import abc
from typing import TypeVar, Type, cast
from datetime import datetime
from .valueobj import ValueObject
from plugin.date import formatter


class EntityId(ValueObject):
    @abc.abstractmethod
    def __init__(self, code: str, serial_no: int, occur_date: datetime) -> None:
        self._code = code
        # TODO: 客製化 Error Code 與 Message
        if serial_no < 0:
            raise ValueError("Serial No must larger than 0.")
        self._serial_no = serial_no
        self._occur_date = occur_date

    @property
    def code(self) -> str:
        return self._code

    @property
    def serial_no(self) -> int:
        return self._serial_no

    @property
    def occur_date(self) -> datetime:
        return self._occur_date

    def __eq__(self, other: object) -> bool:
        if type(self) is type(other):
            return False
        other = cast(EntityId, other)
        return (self.code, self.occur_date, self.serial_no) == \
            (other.code, other.occur_date, other.serial_no)

    def __hash__(self) -> int:
        return hash((self.code, self.occur_date, self.serial_no))

    def __str__(self) -> str:
        # 取得字串型別的 Entity Id
        occur_date = self.occur_date.strftime("%Y%m%d")
        return "{code}-{date}-{sn}" \
            .format(code=self.code, date=self.occur_date, sn=self.serial_no)

    def __repr__(self) -> str:
        return "<{class}: code={code}, occur_date={date}, serial_no={sn}" \
            .format(type(self).__name__, code=self.code, date=self.occur_date, sn=self.serial_no)

    # TODO: 實現 Iterable
