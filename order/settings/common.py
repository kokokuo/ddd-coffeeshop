import os


class BlueprintMapper(object):
    ORDERS_BP = "orders_bp"


class EndpointMapper(object):
    ORDERS_API = "orders_api"
    ORDER_API = "order_api"


class Config(object):
    BLEUPRINTS = BlueprintMapper
    ENDPOINTS = EndpointMapper
    SERVER_PORT = 8000
    # Database settings
    SQL_USERNAME = 'root'
    SQL_PASSWORD = os.environ.get('COFFESHOP_MYSQL_ROOT_PASSWORD', 'Pass@word1')
    SQL_URL = os.environ.get('COFFESHOP_MYSQL_PORT_TCP_ADDR', 'localhost')
    SQL_PORT = os.environ.get('COFFESHOP_MYSQL_PORT_TCP_PORT', '3306')
    SQL_HOST = 'mysql+pymysql://' + SQL_USERNAME + ':' + SQL_PASSWORD + '@' + SQL_URL + ':' + SQL_PORT
    SQL_DATABASE = 'coffeeshop_database'
    SQLALCHEMY_DATABASE_URI = SQL_HOST + '/' + SQL_DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = True
