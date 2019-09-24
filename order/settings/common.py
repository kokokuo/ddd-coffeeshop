import os


class BlueprintMapper(object):
    ORDERS_BP = "orders_bp"


class EndpointMapper(object):
    ORDERS_API = "orders_api"
    ORDER_API = "order_api"


class Config(object):
    BLEUPRINTS = BlueprintMapper
    ENDPOINTS = EndpointMapper
