from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from order.settings import config


blueprint = Blueprint(config.BLEUPRINTS.ORDERS_BP, __name__)
api = Api(blueprint, prefix='/v1.0')


class OrdersResource(Resource):
    pass


class OrderResource(Resource):
    pass
