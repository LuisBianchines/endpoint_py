from flask_restful import Resource
from flask import request 
from models.ProductionOrderM import ProductionOrderModel

class ProductionOrder(Resource):

    def get(self):
        param = request.args.get('search')

        res = ProductionOrderModel.show_production(param)

        return res



        