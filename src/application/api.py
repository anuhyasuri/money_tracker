from flask_restful import Api
from routes.transaction import TransactionRoute
from routes.transactions import TransactionsRoute
from routes.transaction_type import TransactionTypeRoute
from routes.transaction_types import TransactionTypesRoute
from index import application

api = Api(application)

api.add_resource(TransactionRoute, 
				 '/transaction/<id>')
api.add_resource(TransactionsRoute, 
				 '/transactions')

api.add_resource(TransactionTypeRoute, '/transaction_type/<id>')
api.add_resource(TransactionTypesRoute, '/transaction_types')

if __name__ == "__main__":
	application.run(debug=True)
