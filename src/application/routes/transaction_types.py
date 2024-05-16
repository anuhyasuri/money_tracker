from flask_restful import Resource
from service.transaction_type import TransactionTypeService
from flask import request

class TransactionTypesRoute(Resource):
	def get(self):
		data = TransactionTypeService.get_all()
		return data, 200

	def post(self):
		data = request.get_json()
		updated_data = TransactionTypeService.save(data)
		return updated_data, 201
