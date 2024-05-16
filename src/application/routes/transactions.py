from flask_restful import Resource
from service.transaction import TransactionService
from flask import request

class TransactionsRoute(Resource):
	def get(self):
		data = TransactionService.get_all()
		return data, 200
	
	def post(self):
		data = request.get_json()
		updated_data = TransactionService.save(data)
		return updated_data, 201
