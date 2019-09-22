# -*- coding:utf-8 -*-
import uuid
from datetime import datetime, timezone, date
from typing import Optional
from marshmallow import fields, ValidationError


class TimeStamp(fields.Field):
    def _serialize(self, value, attr, obj):
        """
        序列化 datetime 或 date 成 timestamp 的值
        """
        if value is None:
            return None
        # 原本便已經是該型態
        elif isinstance(value, (int, float)) and value >= 0:
            return value
        elif isinstance(value, datetime):
            return value.replace(tzinfo=timezone.utc).timestamp()
        elif isinstance(value, date):
            date_dt = datetime(value.year, value.month, value.day)
            return date_dt.replace(tzinfo=timezone.utc).timestamp()
        raise ValidationError("The type is not date or datetime")


class StrDict(fields.Field):
    def _serialize(self, value, attr, obj):
        """
        序列化 dict 且是 key 與 value 都是 str 的格式為 json (若升到 marshmallow 3.0 即可淘汰)
        """
        if value is None:
            return None
        # 原本便已經是該型態
        if isinstance(value, dict):
            for key, val in value.items():
                if not isinstance(key, str) or not isinstance(val, str):
                    raise ValidationError("The key and value type is not str in dict")
            return value
        raise ValidationError("The type is not dict")