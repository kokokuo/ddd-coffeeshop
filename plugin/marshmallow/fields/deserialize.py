
# -*- coding:utf-8 -*-
import json
from datetime import date
from marshmallow import fields, ValidationError
from werkzeug import datastructures


class FormDict(fields.Field):
    def _deserialize(self, value, attr, data):
        """
        從 Form 的 location 反序列化 json 格式的資料為字典
        """
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        try:
            return json.loads(value)
        except ValidationError as ve:
            raise ve


class FormList(fields.Field):
    def __init__(self, cls_of_list=None, **kwargs) -> None:
        self._cls_of_list = cls_of_list
        super(FormList, self).__init__(**kwargs)

    def _parse_data_of_list(self, value):
        try:
            list_data = json.loads(value)
            for val in list_data:
                if not isinstance(val, self._cls_of_list):
                    raise ValidationError(
                        "the value {val} in the list is not {type} type".format(val=val, type=self._cls_of_list)
                    )
            return list_data
        except ValidationError as ve:
            raise ve

    def _deserialize(self, value, attr, data):
        """
        從 Form 中屬於 List 格式的參數  反序列化 json 後為 list 格式
        """
        if value is None:
            return []
        if isinstance(value, str) and value == '':
            return []
        if isinstance(value, str) and len(value) >= 2:
            if value[0] == '[' and value[len(value) - 1] == ']':
                return self._parse_data_of_list(value)
        raise ValidationError("The format is not belong list.")


class FormNested(fields.Nested):
    def _deserialize(self, value, attr, data):
        """
        對於從 Form 內部取得的 Json 資料，做返序列化後，再傳遞給 Nested 解析
        """
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        try:
            dict_data = json.loads(value)
            # 再丟入 Nested 做解析
            return super()._deserialize(dict_data, attr, data)
        except ValidationError as ve:
            raise ve


class StorageFile(fields.Field):

    def _deserialize(self, value, attr, data):
        """
        從 Form 的 location 反序列化 Request 的檔案
        """
        if value is None:
            return None
        if isinstance(value, datastructures.FileStorage):
            return value
        try:
            return datastructures.FileStorage(value)
        except ValidationError as ve:
            raise ve


class Date(fields.Date):
    def _deserialize(self, value, attr, data):
        """
        強化預設的 Date Field, 在已經是 date 物件時可以直接返回
        """
        if value is None:
            return None
        if isinstance(value, date):
            return value
        try:
            return super()._deserialize(value, attr, data)
        except ValidationError as ve:
            raise ve
