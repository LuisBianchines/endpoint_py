from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from connection import Connection
from db import CreatingDatabaseStructure 
from resources.ProductionOrdersR import ProductionOrder

API_PRODUCTION = '/api/mes/productionothers'

Connection().connect()

CreatingDatabaseStructure.create_structure()

app = Flask('__name__')
app.config['JSON_SORT_KEYS'] = False

CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

api.add_resource(ProductionOrder, API_PRODUCTION)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)  