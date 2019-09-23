# -*- coding:utf-8 -*-
import uuid
import json
import enum
from typing import Optional
from marshmallow import fields
from marshmallow.validate import ValidationError


class Enum(fields.Field):
    def __init__(self, enum_cls=None, **kwargs) -> None:
        self._enum_cls = enum_cls
        super(Enum, self).__init__(**kwargs)

    def _deserialize(self, value, attr, data):
        """
        反序列化成為 Enum
        """
        if self._enum_cls is None:
            err_msg = 'Couldn\'t deserialize, not assign Enum type',
            raise ValidationError(err_msg, field_names=[attr])
        if isinstance(value, self._enum_cls):
            return value
        values = [item.value for item in self._enum_cls]
        if value in values:
            return self._enum_cls(value)
        else:
            err_msg = 'The value not belong to {}'.format(self._enum_cls)
            raise ValidationError(err_msg)

    def _serialize(self, value, attr, obj):
        """
        Enum 序列化成 Enum 的值
        """
        if value is None:
            return None
        elif isinstance(value, enum.Enum):
            return None if value.name in ['Null', 'None'] else value.value
        raise ValidationError("The type is not Enum")


class DateNum(fields.Integer):
    def _deserialize(self, value, attr, data):
        """
        日期號：指定範圍為 1 - 31
        """
        if value is None:
            return None
        if isinstance(value, int):
            if (value >= 1 and value <= 31):
                return value
            raise ValidationError("Date number does not between 1 to 31.")
        try:
            return super()._deserialize(value, attr, data)
        except ValidationError as ve:
            raise ve

    def _serialize(self, value, attr, obj):
        """
        Enum 序列化成 Enum 的值
        """
        if value is None:
            return None
        elif isinstance(value, int):
            if (value >= 1 and value <= 31):
                return value
            raise ValidationError("Date number does not between 1 to 31.")
        try:
            return super()._serialize(value, attr, obj)
        except ValidationError as ve:
            raise ve