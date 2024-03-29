from http import HTTPStatus
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api
from order.settings import config
from order.api.request.order import CreateOrderReqValidator
from order.api.response.order import CreatedOrderResp
from plugin.webargs import parse_reqs
from plugin.speed import profiling

blueprint = Blueprint(config.BLEUPRINTS.ORDERS_BP, __name__)
api = Api(blueprint, prefix='/v1.0')


class OrdersResource(Resource):

    @profiling
    @parse_reqs(CreateOrderReqValidator())
    def post(self, reqargs: dict):
        resp = ("OK", HTTPStatus.OK)
        return resp


class OrderResource(Resource):

    @profiling
    def get(self, id: int):
        resp = ("OK", HTTPStatus.OK)
        return resp


api.add_resource(OrdersResource, "/orders", config.ENDPOINTS.ORDERS_API)
api.add_resource(OrderResource, "/orders/<id>", config.ENDPOINTS.ORDERS_API)
