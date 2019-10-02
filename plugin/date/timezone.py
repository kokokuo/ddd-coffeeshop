import datetime
import pytz

"""
時區換算擴充功能
"""


def utc2local(utc_datetime, timezone_str):
    """
    轉換 utc 時間為指定的 local 時間，如果輸入的時區有錯，則保持原來的 UTC
    Args:
        utc_datetime(datetime): utc 時間
        timezone(str): 指定轉換的時區，採用 tz database 列表
    Returns
        timezone_dt(datetime): 回傳轉換好的時區時間
    """
    # 取得 tzinfo 的時區
    if timezone_str in pytz.common_timezones:
        tz = pytz.timezone(timezone_str)
        # 取得時區資訊的 dateime
        dateime_include_tzinfo = pytz.utc.localize(utc_datetime, is_dst=None)
        timezone_dt = dateime_include_tzinfo.astimezone(tz)
        return timezone_dt
    return utc_datetime


def local2utc(local_datetime, timezone_str):
    """
    轉換 local 時間為指定的 utc 時間，如果輸入的時區有錯，則保持原來的 LOCAL
    Args:
        local_datetime(datetime): local 時間
        timezone(str): 指定轉換的時區，採用 tz database 列表
    Returns
        utc_dt(datetime): 回傳轉換的utc時間
    """
    if timezone_str in pytz.common_timezones:
        local = pytz.timezone(timezone_str)
        # local 時區加入到時間中
        local_dt = local.localize(local_datetime, is_dst=None)
        utc_dt = local_dt.astimezone(pytz.utc)
        return utc_dt

    return local_datetime
